# RAG für strukturierte Daten
Dieses Repository enthält den Code und die Dokumentation zur Bachelorarbeit "Einsatz eines Retrieval-Augmented Generation Systems für die Verarbeitung von Produktdaten aus relationalen Datenbanken im Kontext eines digitalen Einkaufsassistenten ". <br><br>

### Forschungsfrage
Die Forschungsfrage dieser Arbeit lautet: „Wie lässt sich ein Retrieval-Augmented Generation System auf strukturierte Daten aus einer relationalen Datenbank anwenden und wie beeinflussen unterschiedliche Kundenfragen die Qualität des Retrievals und der generierten Antworten?“ <br><br>

### Ordnerstruktur
code/
Enthält den gesamten Quellcode für die Implementierung des RAG-Systems, einschließlich Datenbankanbindung (connect.py), Embedding-Erstellung, sowie Funktionen zur Fragengenerierung, Prompt-Bildung und Interaktion mit dem LLM.

data/
Enthält Beispieldaten und die vorbereiteten JSON- oder CSV-Dateien, die während der Implementierung und Tests genutzt wurden.

docs/
Beinhaltet die wissenschaftliche Dokumentation, darunter die vollständige Bachelorarbeit als PDF, sowie alle relevanten Anhänge.

results/
Hier sind Ergebnisse der Tests und Evaluationen des Systems, wie beispielhafte Fragestellungen, Antworten und Performance-Metriken, abgelegt.

excel/
Enthält die Excel-Dateien mit Fragen und zugehörigen Metadaten, die für die Tests und das Training genutzt wurden.
