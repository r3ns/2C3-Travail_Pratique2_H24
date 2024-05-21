import csv

def pokemons_csv(fichier_csv):
    pokemons = {}
    with open(fichier_csv, newline='') as fichier:
        reader = csv.reader(fichier)
        for ligne in reader:
            nom = ligne[0]
            stats = list(map(int, ligne[1:]))
            pokemons[nom] = stats
    return pokemons

pokemons = pokemons_csv('pokemon.csv')
for nom, stats in pokemons.items():
    print(f"{nom}: {stats}")

pokemons = pokemons_csv("pokemon.csv")
print(isinstance(pokemons, dict))
print(isinstance(pokemons["Pikachu"], list))
print(isinstance(pokemons["Pikachu"][0], int))
