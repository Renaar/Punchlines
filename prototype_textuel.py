import sys
import csv
import random
from colorama import Fore, Back, Style, init

init(autoreset=True)

# Fonction pour effacer l'écran
def effacer_terminal():
    print(Fore.RESET + '\033c', end='')

# Fonction pour attendre la validation du joueur
def attendre_entree():
    input("Appuyez sur Entree pour continuer...")

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
def duel(joueur_punchlines, joueur_reponses, ennemi_punchlines, ennemi_reponses):
    punchlines_ennemi_non_utilisees = ennemi_punchlines
    punchlines_ennemi_utilisees = []
    score_joueur = 0
    score_ennemi = 0

    def avantage_ennemi():
        nonlocal score_joueur
        nonlocal score_ennemi

        if score_joueur < 3 or score_ennemi < 3:
            # Ennemi a l'avantage et envoie une punchline
            effacer_terminal()
            punchline_ennemi = random.choice(punchlines_ennemi_non_utilisees)
            print(f"{Fore.YELLOW}Ennemi dit : {Fore.RED}{punchline_ennemi}")

            # Vérifier si la punchline ennemie est déjà connue par le joueur
            if punchline_ennemi not in joueur_punchlines:
                print(f"{Fore.LIGHTBLUE_EX}Tu apprends une nouvelle punchline !")
                joueur_punchlines.append(punchline_ennemi)
            else:
                print(f"{Fore.LIGHTBLUE_EX}Tu connais déjà cette punchline.")

            # Obtenir la bonne réponse à partir du dictionnaire punchlines_reponses
            bonne_reponse = punchlines_reponses.get(punchline_ennemi)

            # Joueur répond à la punchline de l'ennemi
            print(f"{Fore.YELLOW}Que souhaites-tu répondre ?")
            print()
            for index, element in enumerate(joueur_reponses, start=1):
                print(f"{Fore.YELLOW}{index}) {Fore.CYAN}{element}")
            print()
            reponse_joueur = joueur_reponses[int(input(f"{Fore.YELLOW}Réponse : ")) - 1]
            print()

            # Vérifier si la réponse du joueur est correcte
            if reponse_joueur == bonne_reponse:
                print(f"{Fore.GREEN}Bien joué ! Tu as maintenant l'avantage.")
                score_joueur += 1
                punchlines_ennemi_non_utilisees.remove(punchline_ennemi)
                punchlines_ennemi_utilisees.append(punchline_ennemi)
                print(f"{Fore.CYAN}Joueur : {score_joueur} {Fore.YELLOW}/ {Fore.RED}Ennemi : {score_ennemi}")
                attendre_entree()
                avantage_joueur()

            else:
                print(f"{Fore.RED}Tu as mal répondu, l'ennemi garde l'avantage.")
                score_ennemi += 1
                punchlines_ennemi_non_utilisees.remove(punchline_ennemi)
                punchlines_ennemi_utilisees.append(punchline_ennemi)
                print(f"{Fore.CYAN}Joueur : {score_joueur} {Fore.YELLOW}/ {Fore.RED}Ennemi : {score_ennemi}")
                attendre_entree()
                avantage_ennemi()

        elif score_ennemi == 3:
            print(f"{Fore.YELLOW}Tu as perdu ce duel...")
            punchlines_ennemi_non_utilisees.extend(punchlines_ennemi_utilisees)
            punchlines_ennemi_utilisees.clear()
            effacer_terminal()
            
        elif score_joueur == 3:
            print(f"{Fore.YELLOW}Bravo, tu as gagné ce duel !")
            punchlines_ennemi_non_utilisees.extend(punchlines_ennemi_utilisees)
            punchlines_ennemi_utilisees.clear()
            effacer_terminal()

    def avantage_joueur():
        nonlocal score_joueur
        nonlocal score_ennemi

        if score_joueur < 3 or score_ennemi < 3:
            effacer_terminal()
            # Joueur a l'avantage et choisit la punchline à envoyer
            print(f"{Fore.YELLOW}Choisis ta prochaine punchline :")
            for index, punchline in enumerate(joueur_punchlines, start=1):
                print(f"{Fore.YELLOW}{index}) {Fore.CYAN}{punchline}")
            print()
            punchline_joueur = joueur_punchlines[int(input(f"{Fore.YELLOW}Punchline : ")) - 1]
            print(f"{Fore.CYAN}Joueur dit : {Fore.CYAN}{punchline_joueur}")

            # Obtenir la bonne réponse à partir du dictionnaire punchlines_reponses
            bonne_reponse = punchlines_reponses.get(punchline_joueur)

            # Ennemi répond à la punchline du joueur
            if bonne_reponse in ennemi_reponses:
                reponse_ennemi = bonne_reponse
                print(f"{Fore.YELLOW}Ennemi répond : {Fore.RED}{reponse_ennemi}")
                score_ennemi += 1
                if reponse_ennemi not in joueur_reponses:
                    print(f"{Fore.LIGHTBLUE_EX}Tu apprends une nouvelle réponse !")
                    joueur_reponses.append(reponse_ennemi)

                else:
                    print(f"{Fore.LIGHTBLUE_EX}Tu connais déjà cette réponse.")

                print(f"{Fore.RED}Dommage, l'ennemi t'as eu. Il reprend l'avantage.")
                print(f"{Fore.CYAN}Joueur : {score_joueur} {Fore.YELLOW}/ {Fore.RED}Ennemi : {score_ennemi}")
                attendre_entree()
                effacer_terminal()
                avantage_ennemi()

            else:
                print(f"{Fore.RED}Euuuh... Ah ouais ?!")
                score_joueur += 1
                print(f"{Fore.GREEN}Bien joué, l'ennemi ne sait pas quoi répondre. Tu gardes l'avantage.")
                print(f"{Fore.CYAN}Joueur : {score_joueur} {Fore.YELLOW}/ {Fore.RED}Ennemi : {score_ennemi}")
                attendre_entree()
                effacer_terminal()
                avantage_joueur()

        elif score_ennemi == 3:
            print(f"{Fore.YELLOW}Tu as perdu ce duel...")
            punchlines_ennemi_non_utilisees.extend(punchlines_ennemi_utilisees)
            punchlines_ennemi_utilisees.clear()
            effacer_terminal()

        elif score_joueur == 3:
            print(f"{Fore.YELLOW}Bravo, tu as gagné ce duel !")
            punchlines_ennemi_non_utilisees.extend(punchlines_ennemi_utilisees)
            punchlines_ennemi_utilisees.clear()
            effacer_terminal()
    
    avantage_ennemi()

    #compteur_manche = 1

effacer_terminal()
print("--- C'est l'heure des PUNCHLINES !!! ---")
print()

choix_action = 0

while choix_action != 5:
    #Afficher les options possible
    choix_action = int(input("Que souhaitez-vous faire ? \n 1) Voir ma liste des punchlines/réponses\n 2) Affronter Ennemi A\n 3) Affronter Ennemi B\n 4) Affronter Ennemi C\n 5) Quitter\nChoix : "))

    #Traitement en fonction des choix
    if choix_action == 1:
        punchlines_reponses_connues = []
        effacer_terminal()
        # Ceci permet de n'afficher que les punchlines ou les réponses connues.
        for punchline, reponse in punchlines_reponses.items():
            if punchline in punchlines_joueur and reponse in reponses_joueur:
                punchlines_reponses_connues.append((punchline, reponse))
            elif punchline in punchlines_joueur and reponse not in reponses_joueur:
                punchlines_reponses_connues.append((punchline, "Réponse non apprise"))
            elif punchline not in punchlines_joueur and reponse in reponses_joueur:
                punchlines_reponses_connues.append(("Punchline non apprise", reponse))
            else:
                punchlines_reponses_connues.append(("Punchline non apprise", "Réponse non apprise"))
        print(f"- Punchlines -".ljust(64, '.') + "- Réponses -")
        print()
        for index, i in enumerate(punchlines_reponses_connues, start=1):
            if i[0] == "Punchline non apprise" and i[1] == "Réponse non apprise":
                print(f"{index}) {Fore.RED}{i[0].ljust(60, '.')} / {Fore.RED}{i[1]}")
            elif i[0] != "Punchline non apprise" and i[1] == "Réponse non apprise":
                print(f"{index}) {Fore.GREEN}{i[0].ljust(60, '.')} / {Fore.RED}{i[1]}")
            elif i[0] == "Punchline non apprise" and i[1] != "Réponse non apprise":
                print(f"{index}) {Fore.RED}{i[0].ljust(60, '.')} / {Fore.GREEN}{i[1]}")
            elif i[0] != "Punchline non apprise" and i[1] != "Réponse non apprise":
                print(f"{index}) {Fore.GREEN}{i[0].ljust(60, '.')} / {Fore.GREEN}{i[1]}")
        attendre_entree()
        effacer_terminal()

    elif choix_action == 2:
        duel(punchlines_joueur, reponses_joueur, punchlines_ennemi_A, reponses_ennemi_A)

    elif choix_action == 3:
        duel(punchlines_joueur, reponses_joueur, punchlines_ennemi_B, reponses_ennemi_B)

    elif choix_action == 4:
        duel(punchlines_joueur, reponses_joueur, punchlines_ennemi_C, reponses_ennemi_C)

    elif choix_action == 5:
        print("A bientôt !")
        sys.exit()

    else:
        print("Choix invalide. Veuillez réessayer.")