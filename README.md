# RAG für strukturierte Daten
Dieses Repository enthält den Code und die Dokumentation zur Bachelorarbeit "Einsatz eines Retrieval-Augmented Generation Systems für die Verarbeitung von Produktdaten aus relationalen Datenbanken im Kontext eines digitalen Einkaufsassistenten ". <br><br>

### Forschungsfrage
Die Forschungsfrage dieser Arbeit lautet: „Wie lässt sich ein Retrieval-Augmented Generation System auf strukturierte Daten aus einer relationalen Datenbank anwenden und wie beeinflussen unterschiedliche Kundenfragen die Qualität des Retrievals und der generierten Antworten?“ <br><br>

### Ordnerstruktur
#### code
Enthält den gesamten Quellcode für die Implementierung des RAG-Systems, einschließlich Datenbankanbindung (connect.py). 
Desweiteren ist der Code von den Berechnungen der Ergebnisse und zur Generierung der Abbildungen zu sehen.

#### data
Enthält die eingebundenen Daten aus der relationalen Datenbank, in Form von der Produkttabelle.

#### excel
Enthält drei Exel-Datein mit den Durchläufen 1-3 die stichprobenartig zeigen, dass das RAG immer die gleichen Chunks findet.
Außerdem sind in der Ergebnisse.xlxs Datei die erstellten Fragen, RAG-Antworten und die Bewertung enthalten.
