import json
import csv

def json_a_csv(fichier_json, fichier_csv):
    with open(fichier_json, 'r') as fichier:
        nombrescomplexes = json.load(fichier)

    with open(fichier_csv, 'w', newline='') as fichier:
        writer = csv.writer(fichier)
        for nombre in nombrescomplexes:
            nombre_formate = f"{nombre[0]}{nombre[1]}"
            writer.writerow([nombre_formate])

json_a_csv('data.json', 'nombres_complexes.csv')
