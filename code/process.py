import os
import json
import uuid
import pandas as pd
import chromadb
import chromadb.config
from openai import OpenAI
from datetime import datetime
from icecream import ic

import connect

# paths, they are hardcoded for my local machine, they need to be adjusted for your device
db_path = "C:\\code\\regioshopper_rag\\standard_RAG\\chroma_db"
output_folder_json = "C:\\code\\regioshopper_rag\\standard_RAG\\chunk_documents"
questions_file_path = 'C:\\code\\regioshopper_rag\\standard_RAG\\input\\questions.xlsx'
output_answer_file_path = "C:\\code\\regioshopper_rag\\standard_RAG\\output"
prompt_template_path = "C:\\code\\regioshopper_rag\\standard_RAG\\input\\prompt_template.txt"

# Create the openai and chroma client, the API keys are strored in the environment variables
client_ai = OpenAI()

client_db = chromadb.PersistentClient(path=db_path, settings=chromadb.config.Settings(allow_reset=True))
#client_db.reset()


# Function to get embeddings from OpenAI
def get_embedding(chunks, model="text-embedding-3-large"):
    response = client_ai.embeddings.create(input=chunks, model=model)
    embeddings = [res.embedding for res in response.data]
    
    return embeddings


# Function to save data to a JSON file in a specified folder
def save_to_json(embedding_data, meta_data, filename="data.json"):
    json_data = []
    
    # Iterate through the embedding_data and meta_data lists
    for embedding_record, meta_record in zip(embedding_data, meta_data):
        # Combine all text fields for embedding
        text_to_embed = " ".join([str(value) for value in embedding_record.values()])  
        embedding = get_embedding(text_to_embed)

        # Prepare the structured JSON entry
        json_entry = {
            "id": str(uuid.uuid4()),
            "text": embedding_record,
            "metadata": meta_record,
            "embedding": embedding
        }
        json_data.append(json_entry)
    
    # Construct the full path for the JSON file
    file_path = os.path.join(output_folder_json, filename)
    
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)
    
    print(f"Data successfully saved to {file_path}")


# Create or get the exiting collection from ChromaDB
def get_or_create_collection(collection_name):
    collections = client_db.list_collections()
    collection_names = [collection.name for collection in collections]

    if collection_name in collection_names:
        collection = client_db.get_collection(collection_name)
        print(f"Using existing collection: {collection_name}")
    else:
        collection = client_db.create_collection(collection_name)
        print(f"Created new collection: {collection_name}")
    return collection


# Extract questions from the Excel file
def read_questions_from_excel(file_path, searching_word="questions"):
    df = pd.read_excel(file_path, sheet_name=None)  
    first_sheet_name = list(df.keys())[0]  
    df = df[first_sheet_name]  

    column = None
    for column_name in df.columns:
        if searching_word in column_name:
            column = column_name
            break

    if column and "question_id" in df.columns:  
        # filter only the rows where "true" is set
        if "true" in df.columns:
            df_filtered = df[df["true"] == True]
        else:
            df_filtered = df

        # extract the questions and question_ids
        question_ids = df_filtered["question_id"].tolist()
        questions = df_filtered[column].dropna().tolist()

        # print(f'Found questions in column "{column}": {questions}')
        # print(f'Found question_ids: {question_ids}')

        return df, questions, question_ids, column
    else:
        print(f'No column found containing "{searching_word}" or "question_id" column is missing')
        return df, [], [], None


# Save the Embeddings to ChromaDB
def save_embeddings_to_chromadb(json_file_path, collection_name="documents"):
    # open the JSON file
    with open(json_file_path, encoding="utf-8") as json_file:
        documents = json.load(json_file)
    
    # check if there are any documents in the JSON file
    if len(documents) == 0:
        print(f"No documents found in >{json_file_path}<, skipping adding to ChromaDB")
        return
    
    

    # get or create ChromaDB Collection 
    collection = get_or_create_collection(collection_name)
    
    # Store the documents in the ChromaDB collection
    for doc in documents:
        # flatten the embedding list
        flat_embedding = [item for sublist in doc["embedding"] for item in sublist]
        
        # insert the document into the collection
        collection.add(
            ids=[doc['id']],  
            embeddings=[flat_embedding],  
            documents=[json.dumps(doc['text'], ensure_ascii=False)],  
            metadatas=[doc["metadata"]]  
        )
    
    


# Query the documents in ChromaDB for the questions
def query(questions, n_results=8, collection_name="documents"):
    results = {}
    for question in questions:
        # create the embedding for the question
        response = client_ai.embeddings.create(input=[question], model="text-embedding-3-large")
        query_prompt_embedding = response.data[0].embedding
        
        # get or create the collection
        collection = get_or_create_collection(collection_name)

        # run the query and get the results
        result = collection.query(
            query_embeddings=[query_prompt_embedding],
            n_results=n_results,
            include=["distances", "documents", "metadatas"]
        ) 

        # store the results in the dictionary with the question as the key
        results[question] = result
       
    
    return results

# Function to read the prompt template from a file
def read_prompt_template(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    

# Create and send the prompt to the LLM
def create_and_send_prompt(questions, results, prompt_template_path):
    prompt_prefix = read_prompt_template(prompt_template_path)
    answers = []
    prompts = []

    for question in questions:
        prompt  =f"\n\nHere is the question from the customer: {question}\n"
        
        # get the documents and metadatas from the query results for the current question
        retrieved_docs_list = results[question]['documents']  
        retrieved_metas_list = results[question]['metadatas']  

        prompt += "Here are the documents to answer the questions:\n"
        
        # Iterate through the lists of documents and their corresponding metadata
        for retrieved_docs, retrieved_metas in zip(retrieved_docs_list, retrieved_metas_list):
            for doc_str, metadata in zip(retrieved_docs, retrieved_metas):
                # Extract the id from metadata
                doc_id = metadata.get("id", "Unknown ID")  # Fallback to "Unknown ID" if id is missing

                # Add the document and metadata ID to the prompt
                prompt += f"Document ID: {doc_id}\n"
                prompt += f"Content: {doc_str}\n"

        # Store the generated prompt
        prompts.append(prompt)

        # Create the prompt for the LLM
        messages = [
            {"role": "system", "content": prompt_prefix},
            {"role": "user", "content": prompt}
        ]

        # Send the prompt to the LLM and get the response
        response = client_ai.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0,
            top_p=0.4
        )

        # Extract the answer from the response and store it
        answer = response.choices[0].message.content.strip()
        answers.append(answer)

    return answers, prompts



# fuction to parse the expected IDs from the Excel file
def parse_expected_ids(expected_id_str):
    
    id_list = []
    for part in expected_id_str.split(','):
        part = part.strip()
        if '-' in part:
            start, end = part.split('-')
            id_list.extend(range(int(start), int(end) + 1))
        else:
            id_list.append(int(part))
    return id_list


# Function to compare the IDs with the expected IDs
def compare_ids_with_expected(file_path, results, expected_id_column="expected_data_id", question_column="questions"):
    # extract the data from the Excel file
    df = pd.read_excel(file_path, sheet_name=None)
    first_sheet_name = list(df.keys())[0]
    df = df[first_sheet_name]

    # check if the expected_id_column, question_id column and true column are in the excel file
    if expected_id_column in df.columns and "question_id" in df.columns and "true" in df.columns:
        # filter only the rows where "true" is set
        df_filtered = df[df["true"] == True]

        comparison_results = []
        
        for _, row in df_filtered.iterrows():
            expected_id_str = row[expected_id_column]
            question = row[question_column]

            # convert the expected_id_str to a list of integers
            try:
                expected_ids = parse_expected_ids(str(expected_id_str))
            except ValueError as e:
                print(f"Error parsing expected_data_id for question {question}: {e}")
                comparison_results.append("Parse Error")
                continue

            # extract the document IDs from the query results
            doc_ids = [metadata.get("id") for metadata_list in results[question]['metadatas'] for metadata in metadata_list]
            
            # find the matching and non-matching IDs
            matching_ids = [doc_id for doc_id in doc_ids if doc_id in expected_ids]
            non_matching_ids = [doc_id for doc_id in doc_ids if doc_id not in expected_ids]

            # create the comparison result string`
            match_text = f"Match: {matching_ids}" if matching_ids else "Match: None"
            no_match_text = f"No Match: {non_matching_ids}" if non_matching_ids else "No Match: None"
            comparison_results.append(f"{match_text}, {no_match_text}")
        
        return df_filtered, comparison_results
    else:
        print(f"Spalten '{expected_id_column}', 'question_id' oder 'true' in der Excel-Datei fehlen.")
        return df, []


def save_answers_to_excel(df, question_ids, answers, column_name, prompt, output_file_path, comparison_results):
    timestamp = datetime.now().strftime('%Y_%m_%d__%H_%M')
    output_file = os.path.join(output_file_path, f'_{timestamp}.xlsx')

    # make sure the answers, prompts, and comparison_results have the same length as the question_ids
    if len(answers) < len(question_ids):
        answers.extend([""] * (len(question_ids) - len(answers)))  
    if len(prompt) < len(question_ids):
        prompt.extend([""] * (len(question_ids) - len(prompt)))    

    # create dictionaries to map the question_ids to the answers, prompts, and comparison_results
    answer_dict = {question_id: answer for question_id, answer in zip(question_ids, answers)}
    prompt_dict = {question_id: prmpt for question_id, prmpt in zip(question_ids, prompt)}
    comparison_dict = {question_id: comparison for question_id, comparison in zip(question_ids, comparison_results)}

    # sort the DataFrame by the question_ids
    df[column_name] = df['question_id'].map(answer_dict)        
    df['prompt'] = df['question_id'].map(prompt_dict)           
    df['compared_ids'] = df['question_id'].map(comparison_dict) 

    # make sure the DataFrame does not contain any "Unnamed" columns
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]  

    # store the answers, prompt, and comparison_results in an Excel file
    try:
        df.to_excel(output_file, index=False)  
        print(f"Saved answers, prompt, and ID comparison results to {output_file}")
    except PermissionError:
        print(f"Permission denied: Unable to write to {output_file}. Please check your permissions.")


# Main function to process the data and prepare it for embedding and saving
def process_data(embedding_data, meta_data, questions_file_path):
    
    json_file_path = os.path.join(output_folder_json, "data.json")

    # Save the processed data to a JSON file
    save_to_json(embedding_data, meta_data, filename="data.json")

    #Save the embeddings to ChromaDB
    save_embeddings_to_chromadb(json_file_path)

    # Read the questions from the Excel file
    print(f"Reading questions from {questions_file_path}")
    df, questions,question_ids, _ = read_questions_from_excel(questions_file_path)

    # Execute the query for each question
    print("Executing query for each question")
    query_results = query(questions)

    # create prompt with query results
    print("Creating prompt with query results")
    answers, prompt = create_and_send_prompt(questions, query_results, prompt_template_path)

    # Compare the IDs with the expected IDs
    df, comparison_results = compare_ids_with_expected(questions_file_path, query_results)
    # store answers in Excel file
    save_answers_to_excel(df,question_ids, answers, 'RAG_Antwort', prompt, output_answer_file_path,comparison_results)



# Process the data to create embeddings and save to a JSON file
process_data(connect.embedding_data, connect.meta_data, questions_file_path,)


