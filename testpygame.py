#Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *
import aventure
import time

#Initialisation de la bibliothèque Pygame
pygame.init()

#Ouverture de la fenêtre Pygame
largeur=640*2
hauteur=480*2
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("jeu d'aventure")
font = pygame.font.Font('freesansbold.ttf', 30)

debug ="cc"

def jeu():
    s = aventure.Salle()
    print(s.map)
    loop=s.loop
    if s.get_image():
        image_chemin="image/"
        print(image_chemin+s.get_image())
        fond = pygame.image.load(image_chemin+s.get_image()).convert()
        fenetre.blit(pygame.transform.scale(fond, (largeur,hauteur)),(0,0))
        pygame.display.flip()
    while loop:
        act=""
        for event in pygame.event.get():
            if debug:
                print("event: ",event)
            if event.type == pygame.KEYDOWN:  #lecture du clavier
                act=mouvement(event.key)
                if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                    loop=False
            if event.type == QUIT:
                return "quit"
        if act: 
            s.action(act)
            annonce=s.get_annonce()
            print(annonce)
            fenetre.blit(font.render(annonce, True, (0, 255, 0)),(0,300))
            if debug=="toto":
                y=s.y
                print("x :",s.x,"\ny : ", y)
                print("mur y :\n h :",((y-1)*2)+1)
                print("s :",(y*2)+1)
                print("g :",y*2)
                print("d :",y*2)
            if s.get_image():
                
                image_chemin="image/"
                print(image_chemin+s.get_image())
                fond = pygame.image.load(image_chemin+s.get_image()).convert()
                #fenetre.fill(pygame.Color('white'))
                fenetre.blit(fond, (0,0))
                
                dialogue=pygame.image.load("image/dialogue.png")
                dialogue_x=(largeur/2)-(dialogue.get_size()[0]/2)
                dialogue_y=650
                fenetre.blit(dialogue, (dialogue_x,dialogue_y))
                blit_text(fenetre, annonce, (dialogue_x+30, dialogue_y), font)
                
                pygame.display.flip()
            loop=s.loop
            if loop==False:
                time.sleep(5)

def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def mouvement(e):
    if e==K_LEFT:
        return "q"
    elif e==K_UP:
        return "z"
    elif e==K_RIGHT:
        return "d"
    elif e==K_DOWN:
        return "s"
    else:
        return ""



continuer=1
while continuer:
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
    while continuer==1:
        for event in pygame.event.get():
            print("event: ",event)
            if event.type == QUIT:
                continuer=0
            ## Si le focus est sur la fenêtre.
            if pygame.mouse.get_focused() and pygame.mouse.get_pressed()[0]:
                ## Trouve position de la souris
                x, y = pygame.mouse.get_pos()
                ## S'il y a collision:
                #quit
                collide = quit_bouton.get_rect().collidepoint(x-quit_x, y-quit_y)
                if collide: # 0=gauche, 1=milieu, 2=droite
                    continuer=0
                #play
                collide = play_bouton.get_rect().collidepoint(x-play_x, y-play_y)
                if collide: # 0=gauche, 1=milieu, 2=droite
                    j=jeu()
                    if j=="quit":
                        continuer=0
                        pygame.quit()
                    else:
                        continuer=2
                
