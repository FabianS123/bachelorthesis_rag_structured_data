import mysql.connector
from mysql.connector import Error

# Replace with your MySQL server details
host = 'your_host'
database = 'your_database_name'
user = 'your_username'
password = 'your_password'

try:
    # Establish a connection to the database
    connection = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

    if connection.is_connected():
        print('Successfully connected to the database')

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Define the columns to be selected
        embedding_columns = ["identifier", "price_per_unit", "name", "description", "producer", "brand","origin","supplier","ingredients","categories","category_groups"]

        meta_columns = ["id"]

        all_columns = embedding_columns + meta_columns

        # List of columns as a string
        columns_string = ", ".join(all_columns)

        # Define the SQL query
        query = f"SELECT {columns_string} FROM product"

        # Execute the SQL query
        cursor.execute(query)

        # Fetch the result of the query
        result = cursor.fetchall() #Gucken ob hier direkt dictionary 

        column_names = [i[0] for i in cursor.description]
        

        embedding_data = []
        meta_data = []

        # Iterate over the result 
        for record in result:

            embedding_record = {col: val for col, val in zip(column_names, record) if col in embedding_columns}
            meta_record = {col: val for col, val in zip(column_names, record) if col in meta_columns}
    
            embedding_data.append(embedding_record)
            meta_data.append(meta_record)


except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if connection.is_connected():
        # Close the connection
        connection.close()
        print('MySQL connection is closed')
