import csv
import random

# Fonction pour lire les données d'un fichier CSV
def lire_csv(file_path):
    donnees_csv = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        lecteur_csv = csv.reader(csvfile)
        for ligne in lecteur_csv:
            donnees_csv.append(ligne[0])
    return donnees_csv

#region Creation des listes punchlines, reponses et punchlines-reponses
# Utiliser les données extraites du fichier punchlines.csv
chemin_fichier_csv = "punchlines.csv"
punchlines = lire_csv(chemin_fichier_csv)

# Utiliser les données extraites du fichier reponses.csv
chemin_fichier_csv = "reponses.csv"
reponses = lire_csv(chemin_fichier_csv)

# Utiliser les données extraites du fichier punchlines-reponses.csv
chemin_fichier_csv = "punchlines-reponses.csv"
punchlines_reponses = lire_csv(chemin_fichier_csv)
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

#region Distribution des punchlines et des réponses entre les personnages
# Distribution des punchlines
punchlines_joueur = selectionner_punchlines(punchlines, 3)
punchlines_ennemi_A = selectionner_punchlines(punchlines, 3)
punchlines_ennemi_B = selectionner_punchlines(punchlines, 3)
punchlines_ennemi_C = selectionner_punchlines(punchlines, 3)

# Distribution des réponses
reponses_joueur = selectionner_reponses(reponses, 3)
reponses_ennemi_A = selectionner_reponses(reponses, 3)
reponses_ennemi_B = selectionner_reponses(reponses, 3)
reponses_ennemi_C = selectionner_reponses(reponses, 3)
#endregion

''' Permet d'afficher les punchlines et réponses de chaque personnage (A des fins de déboguage)
# Afficher les punchlines et les réponses disponibles
print("--- Punchlines du joueur ---")
for punchline in punchlines_joueur:
    print(f"{punchline}")

print("--- Réponses du joueur ---")
for reponse in reponses_joueur:
    print(f"{reponse}")

print()

print("--- Punchlines de l'ennemi A ---")
for punchline in punchlines_ennemi_A:
    print(f"{punchline}")

print("--- Réponses de l'ennemi A ---")
for reponse in reponses_ennemi_A:
    print(f"{reponse}")    

print()

print("--- Punchlines de l'ennemi B ---")
for punchline in punchlines_ennemi_B:
    print(f"{punchline}")

print("--- Réponses de l'ennemi B ---")
for reponse in reponses_ennemi_B:
    print(f"{reponse}")  

print()

print("--- Punchlines de l'ennemi C ---")
for punchline in punchlines_ennemi_C:
    print(f"{punchline}")

print("--- Réponses de l'ennemi C ---")
for reponse in reponses_ennemi_C:
    print(f"{reponse}")
'''

# Fonction pour affronter un ennemi
def duel(joueur_punchlines, joueur_reponses, ennemi_punchlines):
    punchline_ennemi = random.choice(ennemi_punchlines)
    print(f"Ennemi dit : {punchline_ennemi}")

    # Vérifier si la punchline ennemie est déjà connue par le joueur
    if punchline_ennemi not in joueur_punchlines:
        print("Tu apprends une nouvelle punchline !")
        print()
        joueur_punchlines.append(punchline_ennemi)
    else:
        print("Tu connais déjà cette punchline.")
        print()

    print("Que souhaites-tu répondre ?")
    print()
    for index, element in enumerate(joueur_reponses, start=1):
        print(f"{index}) {element}")
    print()
    input("Réponse : ")

duel(punchlines_joueur, reponses_joueur, punchlines_ennemi_A)