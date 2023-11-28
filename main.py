import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définir la taille de la fenêtre
largeur_fenetre = 768
hauteur_fenetre = 768
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Politics punchlines")

# Chargez l'image de fond
fond = pygame.image.load("assets/bg/onu.png")  # Remplacez par le chemin de votre image
fond = pygame.transform.scale(fond, (largeur_fenetre, hauteur_fenetre))  # Redimensionnez l'image pour qu'elle corresponde à la fenêtre

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)

# Classe Bouton
class Bouton:
    def __init__(self, x, y, largeur, hauteur, couleur, texte, action=None):
        self.rect = pygame.Rect(x, y, largeur, hauteur)
        self.couleur = couleur
        self.texte = texte
        self.action = action

    def afficher(self):
        pygame.draw.rect(fenetre, self.couleur, self.rect)
        police = pygame.font.Font(None, 36)
        texte = police.render(self.texte, True, NOIR)
        texte_rect = texte.get_rect(center=self.rect.center)
        fenetre.blit(texte, texte_rect)

    def cliquer(self):
        if self.action:
            self.action()

class ZoneDialogue:
    def __init__(self, x, y, largeur, hauteur, couleur_fond, couleur_texte, opacite=255):
        self.rect = pygame.Rect(x, y, largeur, hauteur)
        self.surface = pygame.Surface((largeur, hauteur), pygame.SRCALPHA)
        self.surface.fill((*couleur_fond, opacite))  # Remplir la surface avec la couleur de fond et l'opacité
        self.couleur_texte = couleur_texte
        self.texte = ""

    def afficher(self):
        fenetre.blit(self.surface, self.rect.topleft)  # Afficher la surface à l'emplacement de la fenêtre
        police = pygame.font.Font(None, 24)
        lignes = self.texte.split("\n")
        y = self.rect.y + 10
        for ligne in lignes:
            texte = police.render(ligne, True, self.couleur_texte)
            texte_rect = texte.get_rect(topleft=(self.rect.x + 10, y))
            fenetre.blit(texte, texte_rect)
            y += 30

# Fonction pour mettre à jour le texte de la zone de dialogue
def mettre_a_jour_dialogue(texte):
    zone_dialogue.texte = texte

# Fonction pour commencer le jeu
def commencer_jeu():
    print("Le jeu commence !")  # Remplacez cela par la logique réelle du jeu

# Créer une zone de dialogue
zone_dialogue = ZoneDialogue(50, 350, 700, 200, BLANC, NOIR, opacite=128)

# Créer un bouton "Commencer"
bouton_commencer = Bouton(300, 200, 200, 100, BLANC, "Commencer", commencer_jeu)

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Bouton gauche de la souris
                if bouton_commencer.rect.collidepoint(event.pos):
                    bouton_commencer.cliquer()
                    mettre_a_jour_dialogue("C'EST PARTI !!!")

    fenetre.fill(BLANC)

    # Dessinez l'image de fond
    fenetre.blit(fond, (0, 0))

    # Afficher le bouton "Commencer"
    bouton_commencer.afficher()

    # Afficher la zone de dialogue
    zone_dialogue.afficher()

    pygame.display.flip()
