import matplotlib.pyplot as plt
import os
import numpy as np

# create output folder
output_folder_visuals = "C:\\code\\rag_strutured_data\\standard_RAG\\visuals"


# # function to save the bar chart with error bars for the categories
# def save_trefferquote_balkendiagramm_kategorien(output_folder_visuals):
#     import os
#     import numpy as np
#     import matplotlib.pyplot as plt

    
#     categories = ["Existenzfragen", "Überblicksfragen", "Detailfragen", "Interpretationsfragen", "Synonymfragen", "Toleranzfragen"]
#     trefferquote = [96, 100, 90, 60, 31, 44]
#     standardabweichung = [10.2, 0, 22.8, 38.85, 27.42, 39.29]  

#     # calculate the lower and upper bounds of the error bars
#     lower_bounds = [max(0, tq - sa) for tq, sa in zip(trefferquote, standardabweichung)]
#     upper_bounds = [min(100, tq + sa) for tq, sa in zip(trefferquote, standardabweichung)]
#     error = [
#         [tq - lb for tq, lb in zip(trefferquote, lower_bounds)],
#         [ub - tq for tq, ub in zip(trefferquote, upper_bounds)]
#     ]

#     # create the bar chart
#     fig, ax = plt.subplots()
#     y_pos = np.arange(len(categories))

#     # background lines
#     ax.set_yticks(np.arange(0, 101, 10))
#     ax.yaxis.grid(True, linestyle='--', alpha=0.5)

#     # bar width
#     bar_width = 0.5

#     # draw the original bars with error bars
#     ax.bar(y_pos, trefferquote, width=bar_width, color='skyblue', edgecolor='black', label='Trefferquote',
#            yerr=error, capsize=7, error_kw={'elinewidth': 1, 'capthick': 1, 'capsize': 7})

#     # title and axis labels
#     ax.set_xticks(y_pos)
#     ax.set_xticklabels(categories, rotation=45, ha="right")
#     ax.set_yticks(np.arange(0, 101, 10))
#     ax.set_ylim(0, 100)
#     ax.set_ylabel("$\\bar{x}$  Trefferquote")
#     ax.set_xlabel("Fragekategorien")

#     # Legende hinzufügen
#     #ax.legend()

#     # Formatieren der Y-Achse mit Prozentwerten
#     ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}%'))


    



#     # Plot speichern
#     os.makedirs(output_folder_visuals, exist_ok=True)
#     output_path = os.path.join(output_folder_visuals, "Trefferquote_Kategorien_fehlerbalken_final.png")

#     # Platz für Achsentexte garantieren
#     plt.tight_layout()
#     plt.savefig(output_path, dpi=300)

#     print(f"Das Diagramm wurde gespeichert unter: {output_path}")





def save_trefferanzahl_Kriterien(output_folder_visuals):

    # Kategorien und Trefferanzahl
    categories = [
        "Kriterium 1", "Kriterium 2", "Kriterium 3", "Kriterium 4", "Kriterium 5"
    ]
    trefferanzahl = [88.9, 91.1, 93.3, 73.3, 60]

    # Balkendiagramm erstellen
    fig, ax = plt.subplots(figsize=(6, 4))  # Einheitliche Größe wie andere Diagramme
    y_pos = np.arange(len(categories))

    # Hintergrundlinien einfügen
    ax.set_yticks(np.arange(0, 101, 10))
    ax.yaxis.grid(True, linestyle='--', alpha=0.5)

    # Balkenbreite
    bar_width = 0.4  # Schmalere Balken für Konsistenz

    # Ursprüngliche Balken zeichnen
    ax.bar(y_pos, trefferanzahl, width=bar_width, color='cornflowerblue')

    # Anpassung der X-Achse
    ax.set_xticks(y_pos)
    ax.set_xticklabels(categories, rotation=45, ha="right")  # Konsistente Drehung der Kategorien

    # Achsenbeschriftung
    ax.set_yticks(np.arange(0, 101, 10))
    ax.set_ylim(0, 100)
    ax.set_ylabel("$\\bar{x}$ Fragen mit erfüllten Kriterien")
    ax.set_xlabel("Bewertungskriterien")

    # Formatieren der Y-Achse mit Prozentwerten
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}%'))

    # Legende hinzufügen
    legend_labels = [
        "Kriterium 1: Wurde die Frage erkannt?",
        "Kriterium 2: Bezieht sich die Antwort direkt auf die Frage?",
        "Kriterium 3: Sind die Informationen in der Antwort faktisch korrekt und mit den\n                    zugrunde liegenden Daten konsistent?",
        "Kriterium 4: Wurden falsche Informationen in der Antwort vermieden?",
        "Kriterium 5: Wurde die Intention der Frage korrekt interpretiert?"
    ]

    # Legende unterhalb des Plots platzieren
    fig.text(
        0.05, 0.02,  # Position unterhalb des Diagramms linksbündig
        "\n".join(legend_labels),
        wrap=True, horizontalalignment='left', fontsize=9
    )

    # Platz für Achsentexte und Legende garantieren
    plt.tight_layout(rect=[0, 0.2, 1, 1])  # Platz für die Legende einplanen

    # Plot speichern
    os.makedirs(output_folder_visuals, exist_ok=True)
    output_path = os.path.join(output_folder_visuals, "Trefferquote_Fragetyp_proportionen_test10.png")
    plt.savefig(output_path, dpi=300,)

    print(f"Das Diagramm wurde gespeichert unter: {output_path}")


def save_trefferquote_type_fehlerbalken(output_folder_visuals):
    import os
    import numpy as np
    import matplotlib.pyplot as plt

    # Kategorien, Trefferquote und Standardabweichung
    categories = ["Geschlossene Fragen", "Offene Fragen"]
    trefferquote = [68, 65]
    standardabweichung = [40.38, 36.74]  # Neue Werte für Standardabweichung

    # Berechnung der unteren und oberen Grenzen der Fehlerbalken
    lower_bounds = [max(0, tq - sa) for tq, sa in zip(trefferquote, standardabweichung)]
    upper_bounds = [min(100, tq + sa) for tq, sa in zip(trefferquote, standardabweichung)]
    error = [
        [tq - lb for tq, lb in zip(trefferquote, lower_bounds)],
        [ub - tq for tq, ub in zip(trefferquote, upper_bounds)]
    ]

    # X-Positionen für die Balken
    y_pos = np.arange(len(categories))

    # Balkendiagramm erstellen
    fig, ax = plt.subplots(figsize=(6, 4))  # Anpassung der Größe für ein vergleichbares Sichtfeld

    # Hintergrundlinien einfügen
    ax.set_yticks(np.arange(0, 101, 10))
    ax.yaxis.grid(True, linestyle='--', alpha=0.5)

    # Balkenbreite
    bar_width = 0.3  # Schmalere Balken

    # Balken mit Fehlerbalken zeichnen
    ax.bar(y_pos, trefferquote, width=bar_width, color='skyblue', edgecolor='black', 
           yerr=error, capsize=7, error_kw={'elinewidth': 1, 'capthick': 1, 'capsize': 7})

    # Anpassung der X-Achse zur Zentrierung
    ax.set_xlim(-0.5, len(categories) - 0.5)  # Platz um die Balken zentriert halten

    # Achsenbeschriftung und Titel
    ax.set_xticks(y_pos)
    ax.set_xticklabels(categories, rotation=45, ha="right")  # Gleiche Ausrichtung
    ax.set_yticks(np.arange(0, 101, 10))
    ax.set_ylim(0, 100)
    ax.set_ylabel("$\\bar{x}$  Trefferquote")
    ax.set_xlabel("Fragetypen")

    # Legende hinzufügen
    #ax.legend()

    # Formatieren der Y-Achse mit Prozentwerten
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}%'))

    # Platz für Achsentexte garantieren
    plt.tight_layout()

    # Plot speichern
    os.makedirs(output_folder_visuals, exist_ok=True)
    output_path = os.path.join(output_folder_visuals, "Trefferquote_Fragetyp_fehlerbalken_final.png")
    plt.savefig(output_path, dpi=300)

    print(f"Das Diagramm wurde gespeichert unter: {output_path}")


# function to save the bar chart with error bars for the types
def test_save_trefferquote_type_fehlerbalken(output_folder_visuals):
    import os
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D

    # categories, hit rate, and standard deviation
    categories = ["Geschlossene Fragen", "Offene Fragen"]
    trefferquote = [68, 65]
    standardabweichung = [40.38, 36.74]  

    # calculate the lower and upper bounds of the error bars
    lower_bounds = [max(0, tq - sa) for tq, sa in zip(trefferquote, standardabweichung)]
    upper_bounds = [min(100, tq + sa) for tq, sa in zip(trefferquote, standardabweichung)]
    error = [
        [tq - lb for tq, lb in zip(trefferquote, lower_bounds)],
        [ub - tq for tq, ub in zip(trefferquote, upper_bounds)]
    ]

    # x positions for the bars
    y_pos = np.arange(len(categories))

    # create the bar chart
    fig, ax = plt.subplots(figsize=(6, 4))  

    # background lines
    ax.set_yticks(np.arange(0, 101, 10))
    ax.yaxis.grid(True, linestyle='--', alpha=0.5)

    # bar width
    bar_width = 0.3  

    # bar chart with error bars
    ax.bar(y_pos, trefferquote, width=bar_width, color='skyblue', edgecolor='black', 
           yerr=error, capsize=7, error_kw={'elinewidth': 1, 'capthick': 1, 'capsize': 7})

    # axis labels and title
    ax.set_xlim(-0.5, len(categories) - 0.5)  

    # 
    ax.set_xticks(y_pos)
    ax.set_xticklabels(categories, rotation=45, ha="right")  # 
    ax.set_ylim(0, 100)
    ax.set_ylabel("Mittelwert Trefferquote")
    ax.set_xlabel("Fragetypen")

    # format the y-axis with percentage values
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}%'))

    # legend
    legend_elements = [
        Line2D([0], [0], color='skyblue', lw=4, label='Trefferquote'),
        Line2D([0], [0], color='black', lw=1, label='Standardabweichung')
    ]
    ax.legend(
        handles=legend_elements,
        loc='upper right',
        fontsize=8,  
        frameon=True,  
        labelspacing=0.5  
    )

    # provide space for axis labels
    plt.tight_layout()

    # save the plot
    os.makedirs(output_folder_visuals, exist_ok=True)
    output_path = os.path.join(output_folder_visuals, "test.png")
    plt.savefig(output_path, dpi=300, bbox_inches="tight")

    print(f"Das Diagramm wurde gespeichert unter: {output_path}")


# function to save the bar chart with error bars for the categories
def test_save_trefferquote_balkendiagramm_kategorien(output_folder_visuals):
    import os
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D

    # categories, hit rate, and standard deviation
    categories = ["Existenzfragen", "Überblicksfragen", "Detailfragen", "Interpretationsfragen", "Synonymfragen", "Toleranzfragen"]
    trefferquote = [96, 100, 90, 60, 31, 44]
    standardabweichung = [10.2, 0, 22.8, 38.85, 27.42, 39.29]  # Neue Werte für Standardabweichung

    # calculate the lower and upper bounds of the error bars
    lower_bounds = [max(0, tq - sa) for tq, sa in zip(trefferquote, standardabweichung)]
    upper_bounds = [min(100, tq + sa) for tq, sa in zip(trefferquote, standardabweichung)]
    error = [
        [tq - lb for tq, lb in zip(trefferquote, lower_bounds)],
        [ub - tq for tq, ub in zip(trefferquote, upper_bounds)]
    ]

    # bar chart
    fig, ax = plt.subplots()
    y_pos = np.arange(len(categories))

    # background lines
    ax.set_yticks(np.arange(0, 101, 10))
    ax.yaxis.grid(True, linestyle='--', alpha=0.5)

    # bar width
    bar_width = 0.5

    # draw the original bars with error bars
    ax.bar(y_pos, trefferquote, width=bar_width, color='skyblue', edgecolor='black', 
           yerr=error, capsize=7, error_kw={'elinewidth': 1, 'capthick': 1, 'capsize': 7})

    # axis labels and title
    ax.set_xticks(y_pos)
    ax.set_xticklabels(categories, rotation=45, ha="right")
    ax.set_yticks(np.arange(0, 101, 10))
    ax.set_ylim(0, 100)
    ax.set_ylabel("Mittelwert Trefferquote")
    ax.set_xlabel("Fragekategorien")

    # format the y-axis with percentage values
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}%'))

    # legend
    legend_elements = [
        Line2D([0], [0], color='skyblue', lw=4, label='Trefferquote'),
        Line2D([0], [0], color='black', lw=1, label='Standardabweichung')
    ]
    ax.legend(
        handles=legend_elements,
        loc='upper right',  
        fontsize=8,         
        frameon=True,       
        labelspacing=0.5    
    )

    # space for axis labels 
    plt.tight_layout()

    # save the plot
    os.makedirs(output_folder_visuals, exist_ok=True)
    output_path = os.path.join(output_folder_visuals, "Trefferquote_Kategorien_fehlerbalken_test.png")
    plt.savefig(output_path, dpi=300)

    print(f"Das Diagramm wurde gespeichert unter: {output_path}")



# functions to save the charts as images
save_trefferanzahl_Kriterien(output_folder_visuals)
#test_save_trefferquote_type_fehlerbalken(output_folder_visuals)
#test_save_trefferquote_balkendiagramm_kategorien(output_folder_visuals)