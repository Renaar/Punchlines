import sys
import csv
import random
from colorama import Fore, Back, Style, init

init(autoreset=True)

compteur_victoires = 0
compteur_defaites = 0
punchlines_apprises = 0
reponses_apprises = 0

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

# Fonction pour affronter un ennemi
def duel(joueur_punchlines, joueur_reponses, ennemi_punchlines, ennemi_reponses):
    punchlines_ennemi_non_utilisees = ennemi_punchlines
    punchlines_ennemi_utilisees = []
    score_joueur = 0
    score_ennemi = 0
    compteur_manche = 1

    # Phase où l'ennemi a l'avantage et envoie une punchline. Le joueur doit répondre.
    def avantage_ennemi():
        nonlocal score_joueur
        nonlocal score_ennemi
        nonlocal compteur_manche
        global compteur_victoires
        global compteur_defaites

        if score_joueur != 3 and score_ennemi != 3:
            # Ennemi a l'avantage et envoie une punchline
            effacer_terminal()
            print(f"{Fore.YELLOW}--- Manche {compteur_manche} ---")
            print()
            punchline_ennemi = random.choice(punchlines_ennemi_non_utilisees)
            print(f"{Fore.YELLOW}Ennemi dit : {Fore.RED}{punchline_ennemi}")
            # Vérifier si la punchline ennemie est déjà connue par le joueur

            if punchline_ennemi not in joueur_punchlines:
                print(f"{Fore.LIGHTBLUE_EX}Tu apprends une nouvelle punchline !")
                joueur_punchlines.append(punchline_ennemi)
                print()
            else:
                print(f"{Fore.LIGHTBLUE_EX}Tu connais déjà cette punchline.")
                print()

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
            print(f"{Fore.YELLOW}Joueur répond : {Fore.CYAN}{reponse_joueur}")
            print()

            # Vérifier si la réponse du joueur est correcte
            if reponse_joueur == bonne_reponse:
                print(f"{Fore.GREEN}Bien joué ! Tu as maintenant l'avantage.")
                score_joueur += 1
                compteur_manche += 1
                punchlines_ennemi_non_utilisees.remove(punchline_ennemi)
                punchlines_ennemi_utilisees.append(punchline_ennemi)
                print(f"{Fore.CYAN}Joueur : {score_joueur} {Fore.YELLOW}/ {Fore.RED}Ennemi : {score_ennemi}")
                print()
                attendre_entree()
                avantage_joueur()
            else:
                print(f"{Fore.RED}Tu as mal répondu, l'ennemi garde l'avantage.")
                score_ennemi += 1
                compteur_manche += 1
                punchlines_ennemi_non_utilisees.remove(punchline_ennemi)
                punchlines_ennemi_utilisees.append(punchline_ennemi)
                print(f"{Fore.CYAN}Joueur : {score_joueur} {Fore.YELLOW}/ {Fore.RED}Ennemi : {score_ennemi}")
                print()
                attendre_entree()
                avantage_ennemi()
        
        if score_ennemi == 3:
            effacer_terminal()
            print(f"{Fore.YELLOW}Tu as perdu ce duel...")
            print()
            print(f"{Fore.CYAN}Joueur : {score_joueur} {Fore.YELLOW}/ {Fore.RED}Ennemi : {score_ennemi}")
            punchlines_ennemi_non_utilisees.extend(punchlines_ennemi_utilisees)
            punchlines_ennemi_utilisees.clear()
            compteur_defaites += 1
            print()
            attendre_entree()
            boucle_principale_jeu()

        elif score_joueur == 3:
            effacer_terminal()
            print(f"{Fore.YELLOW}Bravo, tu as gagné ce duel !")
            print()
            print(f"{Fore.CYAN}Joueur : {score_joueur} {Fore.YELLOW}/ {Fore.RED}Ennemi : {score_ennemi}")
            punchlines_ennemi_non_utilisees.extend(punchlines_ennemi_utilisees)
            punchlines_ennemi_utilisees.clear()
            compteur_victoires += 1
            print()
            attendre_entree()
            boucle_principale_jeu()

    # Phase où le joueur a l'avantage et envoie une punchline. L'ennemi doit répondre.
    def avantage_joueur():
        nonlocal score_joueur
        nonlocal score_ennemi
        nonlocal compteur_manche
        global compteur_victoires
        global compteur_defaites

        if score_joueur != 3 and score_ennemi != 3:
            print(f"{Fore.YELLOW}--- Manche {compteur_manche} ---")
            print()
            # Joueur a l'avantage et choisit la punchline à envoyer
            effacer_terminal()
            print(f"{Fore.YELLOW}Tu as l'avantage !")
            print(f"{Fore.YELLOW}Choisis ta prochaine punchline :")
            for index, punchline in enumerate(joueur_punchlines, start=1):
                print(f"{Fore.YELLOW}{index}) {Fore.CYAN}{punchline}")
            print()
            punchline_joueur = joueur_punchlines[int(input(f"{Fore.YELLOW}Punchline : ")) - 1]
            print()
            print(f"{Fore.YELLOW}Joueur dit : {Fore.CYAN}{punchline_joueur}")
            print()
            # Obtenir la bonne réponse à partir du dictionnaire punchlines_reponses
            bonne_reponse = punchlines_reponses.get(punchline_joueur)
            # Ennemi répond à la punchline du joueur
            if bonne_reponse in ennemi_reponses:
                reponse_ennemi = bonne_reponse
                print(f"{Fore.YELLOW}Ennemi répond : {Fore.RED}{reponse_ennemi}")
                score_ennemi += 1
                compteur_manche += 1
                if reponse_ennemi not in joueur_reponses:
                    print(f"{Fore.LIGHTBLUE_EX}Tu apprends une nouvelle réponse !")
                    joueur_reponses.append(reponse_ennemi)
                    print()
                else:
                    print(f"{Fore.LIGHTBLUE_EX}Tu connais déjà cette réponse.")
                    print()
                print(f"{Fore.RED}Dommage, l'ennemi t'as eu. Il reprend l'avantage.")
                print(f"{Fore.CYAN}Joueur : {score_joueur} {Fore.YELLOW}/ {Fore.RED}Ennemi : {score_ennemi}")
                print()
                attendre_entree()
                avantage_ennemi()
            else:
                print(f"{Fore.YELLOW}Ennemi répond : {Fore.RED}Euuuh... Ah ouais ?!")
                score_joueur += 1
                compteur_manche += 1
                print()
                print(f"{Fore.GREEN}Bien joué, l'ennemi ne sait pas quoi répondre. Tu gardes l'avantage.")
                print(f"{Fore.CYAN}Joueur : {score_joueur} {Fore.YELLOW}/ {Fore.RED}Ennemi : {score_ennemi}")
                print()
                attendre_entree()
                avantage_joueur()

        if score_ennemi == 3:
            effacer_terminal()
            print(f"{Fore.YELLOW}Tu as perdu ce duel...")
            print()
            print(f"{Fore.CYAN}Joueur : {score_joueur} {Fore.YELLOW}/ {Fore.RED}Ennemi : {score_ennemi}")
            punchlines_ennemi_non_utilisees.extend(punchlines_ennemi_utilisees)
            punchlines_ennemi_utilisees.clear()
            compteur_defaites += 1
            print()
            attendre_entree()
            boucle_principale_jeu()

        elif score_joueur == 3:
            effacer_terminal()
            print(f"{Fore.YELLOW}Bravo, tu as gagné ce duel !")
            print()
            print(f"{Fore.CYAN}Joueur : {score_joueur} {Fore.YELLOW}/ {Fore.RED}Ennemi : {score_ennemi}")
            punchlines_ennemi_non_utilisees.extend(punchlines_ennemi_utilisees)
            punchlines_ennemi_utilisees.clear()
            compteur_victoires += 1
            print()
            attendre_entree()
            boucle_principale_jeu()
    
    print(f"{Fore.YELLOW}C'est l'heure... du.... {Fore.RED}DU {Fore.BLUE}DU {Fore.GREEN}DU {Fore.MAGENTA}DU{Fore.BLACK}DU{Fore.WHITE}DU... {Fore.RED}DUEL !")
    print()
    attendre_entree()
    avantage_ennemi()

def fin_jeu():
    print()
    print(f"{Fore.GREEN}BIEN JOUÉ ! Vous avez appris toutes les punchlines et toutes les réponses !\n\nMerci d'avoir joué et à bientôt !")
    print()
    attendre_entree()
    sys.exit()

# Boucle principale du jeu
def boucle_principale_jeu():
    global punchlines_apprises
    global reponses_apprises
    punchline_dans_dictionnaire = [element for element in punchlines_joueur if element in punchlines_reponses]
    punchlines_apprises = len(punchline_dans_dictionnaire)
    reponse_dans_dictionnaire = [element for element in reponses_joueur if element in punchlines_reponses.values()]
    reponses_apprises = len(reponse_dans_dictionnaire)

    effacer_terminal()
    print(f"{Fore.RED}--- PUNCHLINES ---")
    print()
    choix_action = 0
    while choix_action != 5:
        #Afficher les options possible
        print(f"{Fore.GREEN}Victoires : {compteur_victoires} / {Fore.RED}Défaites : {compteur_defaites}")
        print()
        if punchlines_apprises != 12 and reponses_apprises != 12:
            print(f"Punchlines apprises : {punchlines_apprises} / 12\nRéponses apprises : {reponses_apprises} / 12")
        elif punchlines_apprises == 12 and reponses_apprises != 12:
            print(f"{Fore.GREEN}Vous avez appris toutes les punchlines !\n{Fore.WHITE}Réponses apprises : {reponses_apprises} / 12")
        else:
            fin_jeu()
        print()
        choix_action = int(input(f"{Fore.YELLOW}Que souhaitez-vous faire ? \n\n {Fore.CYAN}1) Voir ma liste des punchlines/réponses\n {Fore.RED}2) Affronter Ennemi A\n 3) Affronter Ennemi B\n 4) Affronter Ennemi C\n {Fore.MAGENTA}5) Quitter\n\n{Fore.YELLOW}Choix : "))
        print()
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
            print()
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

boucle_principale_jeu()