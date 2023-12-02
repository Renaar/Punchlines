def choisir_reponse_ennemi(punchline, ennemi_reponses):
    # Vérifier si l'ennemi connaît la réponse à la punchline du joueur
    if punchline in ennemi_reponses:
        return ennemi_reponses[punchline]
    else:
        # Si l'ennemi ne connaît pas la réponse, il répond n'importe quoi
        return "Réponse aléatoire de l'ennemi"

def duel(joueur_punchlines, joueur_reponses, ennemi_punchlines, ennemi_reponses):
    compteur_manche = 1
    score_joueur = 0
    score_ennemi = 0
    punchlines_ennemi_non_utilisees = ennemi_punchlines
    punchlines_ennemi_utilisees = []

    while score_joueur < 3 and score_ennemi < 3:
        effacer_terminal()
        print(f"{Fore.YELLOW}--- Manche {compteur_manche} ---")

        # Ennemi envoie une punchline
        punchline_ennemi = random.choice(punchlines_ennemi_non_utilisees)
        print(f"{Fore.YELLOW}Ennemi dit : {Fore.RED}{punchline_ennemi}")

        # Vérifier si la punchline ennemie est déjà connue par le joueur
        if punchline_ennemi not in joueur_punchlines:
            print(f"{Fore.LIGHTBLUE_EX}Tu apprends une nouvelle punchline !")
            joueur_punchlines.append(punchline_ennemi)
        else:
            print(f"{Fore.LIGHTBLUE_EX}Tu connais déjà cette punchline.")

        # Joueur répond à la punchline de l'ennemi
        print(f"{Fore.YELLOW}Que souhaites-tu répondre ?")
        print()
        for index, element in enumerate(joueur_reponses, start=1):
            print(f"{Fore.YELLOW}{index}) {Fore.CYAN}{element}")
        print()
        reponse_joueur = joueur_reponses[int(input(f"{Fore.YELLOW}Réponse : ")) - 1]
        print()

        # Vérifier si la réponse du joueur est correcte
        if reponse_joueur == choisir_reponse_ennemi(punchline_ennemi, ennemi_reponses):
            print(f"{Fore.GREEN}Bien joué ! Tu as maintenant l'avantage.")
            score_joueur += 1

            # Joueur choisit la punchline à envoyer
            print(f"{Fore.YELLOW}Choisis ta prochaine punchline :")
            for index, punchline in enumerate(joueur_punchlines, start=1):
                print(f"{Fore.YELLOW}{index}) {Fore.CYAN}{punchline}")
            print()
            punchline_joueur = joueur_punchlines[int(input(f"{Fore.YELLOW}Punchline : ")) - 1]
            print(f"{Fore.CYAN}Joueur dit : {Fore.RED}{punchline_joueur}")

            # Ennemi répond à la punchline du joueur
            reponse_ennemi = choisir_reponse_ennemi(punchline_joueur, ennemi_reponses)

            # Vérifier si la réponse de l'ennemi est connue du joueur
            if reponse_ennemi not in joueur_reponses:
                print(f"{Fore.LIGHTBLUE_EX}Tu apprends une nouvelle réponse !")
                joueur_reponses.append(reponse_ennemi)
        else:
            print(f"{Fore.RED}Tu as mal répondu, l'ennemi garde l'avantage.")
            score_ennemi += 1

        punchlines_ennemi_non_utilisees.remove(punchline_ennemi)
        punchlines_ennemi_utilisees.append(punchline_ennemi)
        compteur_manche += 1
        print(f"{Fore.CYAN}Joueur : {score_joueur} {Fore.YELLOW}/ {Fore.RED}Ennemi : {score_ennemi}")
        attendre_entree()

    if score_ennemi == 3:
        print(f"{Fore.YELLOW}Tu as perdu ce duel...")
        punchlines_ennemi_non_utilisees.extend(punchlines_ennemi_utilisees)
        punchlines_ennemi_utilisees.clear()
        effacer_terminal()
    elif score_joueur == 3:
        print(f"{Fore.YELLOW}Bravo, tu as gagné ce duel !")
        punchlines_ennemi_non_utilisees.extend(punchlines_ennemi_utilisees)
        punchlines_ennemi_utilisees.clear()
        effacer_terminal()
