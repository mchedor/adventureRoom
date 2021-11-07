#Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *
import aventure

def jeu():
    s = aventure.Salle()
    





#Initialisation de la bibliothèque Pygame
pygame.init()

#Ouverture de la fenêtre Pygame
largeur=640*2
hauteur=480*2
fenetre = pygame.display.set_mode((largeur, hauteur))

#Chargement et collage du fond
image_chemin="image/menu/"
fond = pygame.image.load(image_chemin+"fond.png").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
titre = pygame.image.load(image_chemin+"titre.png").convert_alpha()
titre_x=(largeur/2)-(titre.get_size()[0]/2)
titre_y=50
fenetre.blit(titre, (titre_x,titre_y))

play_bouton = pygame.image.load(image_chemin+"play_button.png").convert_alpha()
play_x=(largeur/2)-(play_bouton.get_size()[0]/2)
play_y=300
fenetre.blit(play_bouton, (play_x,play_y))

quit_bouton = pygame.image.load(image_chemin+"quit_button.png").convert_alpha()
quit_x=(largeur/2)-(quit_bouton.get_size()[0]/2)
quit_y=400
fenetre.blit(quit_bouton, (quit_x,quit_y))


#Rafraîchissement de l'écran
pygame.display.flip()

print(play_bouton.get_rect())
#BOUCLE INFINIE
continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer=0
        ## Si le focus est sur la fenêtre.
        if pygame.mouse.get_focused() and pygame.mouse.get_pressed()[0]:
            ## Trouve position de la souris
            x, y = pygame.mouse.get_pos()
            ## S'il y a collision:
            #play
            collide = play_bouton.get_rect().collidepoint(x-play_x, y-play_y)
            if collide: # 0=gauche, 1=milieu, 2=droite
                jeu()
            #quit
            collide = quit_bouton.get_rect().collidepoint(x-quit_x, y-quit_y)
            if collide: # 0=gauche, 1=milieu, 2=droite
                continuer=0
