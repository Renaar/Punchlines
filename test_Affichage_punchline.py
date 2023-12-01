import sys
import csv
import random
from colorama import Fore, Back, Style, init

init(autoreset=True)

# Fonction pour lire les données d'un fichier CSV et créer un dictionnaire
def lire_csv_dictionnaire(file_path):
    donnees_csv = {}
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        lecteur_csv = csv.reader(csvfile)
        for ligne in lecteur_csv:
                punchline, reponse = ligne[0], ligne[1]
                donnees_csv[punchline] = reponse
    return donnees_csv

#region Creation du dictionnaire punchlines-reponses et des listes punchlines, reponses

# Utiliser les données extraites du fichier punchlines-reponses.csv pour créer le dictionnaire
chemin_fichier_csv = "punchlines-reponses.csv"
punchlines_reponses = lire_csv_dictionnaire(chemin_fichier_csv)

#Créer les listes punchlines et réponses qui seront distribuées aux ennemis
punchlines = list(punchlines_reponses.keys())
reponses = list(punchlines_reponses.values())

#endregion

# Fonction pour sélectionner aléatoirement 3 punchlines parmi la liste punchlines et les retire de la liste
def selectionner_punchlines(punchlines, nombre):
    punchlines_selectionnees = random.sample(punchlines, nombre)
    for i in punchlines_selectionnees:
        punchlines.remove(i)
    return punchlines_selectionnees

# Fonction pour sélectionner aléatoirement 3 réponses parmi la liste reponses et les retire de la liste
def selectionner_reponses(reponses, nombre):
    reponses_selectionnees = random.sample(reponses, nombre)
    for i in reponses_selectionnees:
        reponses.remove(i)
    return reponses_selectionnees

punchlines_joueur = selectionner_punchlines(punchlines, 3)
reponses_joueur = selectionner_reponses(reponses, 3)

punchlines_reponses_connues = []

for punchline, reponse in punchlines_reponses.items():
    if punchline in punchlines_joueur and reponse in reponses_joueur:
        punchlines_reponses_connues.append((punchline, reponse))
    elif punchline in punchlines_joueur and reponse not in reponses_joueur:
        punchlines_reponses_connues.append((punchline, "Réponse non apprise"))
    elif punchline not in punchlines_joueur and reponse in reponses_joueur:
        punchlines_reponses_connues.append(("Punchline non apprise", reponse))
    else:
        punchlines_reponses_connues.append(("Punchline non apprise", "Réponse non apprise"))

for index, i in enumerate(punchlines_reponses_connues, start=1):
    if i[0] == "Punchline non apprise" and i[1] == "Réponse non apprise":
        print(f"{index}) {Fore.RED}{i[0]} / {Fore.RED}{i[1]}")
    elif i[0] != "Punchline non apprise" and i[1] == "Réponse non apprise":
        print(f"{index}) {Fore.GREEN}{i[0]} / {Fore.RED}{i[1]}")
    elif i[0] == "Punchline non apprise" and i[1] != "Réponse non apprise":
        print(f"{index}) {Fore.RED}{i[0]} / {Fore.GREEN}{i[1]}")
    elif i[0] != "Punchline non apprise" and i[1] != "Réponse non apprise":
        print(f"{index}) {Fore.GREEN}{i[0]} / {Fore.GREEN}{i[1]}")