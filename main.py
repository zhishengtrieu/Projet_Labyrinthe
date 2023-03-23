import pygame
from Laby import *
from button import *

# on initialise la longueur et la hauteur du labyrinthe
longueur, hauteur = 10, 10

# la taille de la fenêtre du jeu
window_height, window_width = 700, 700

pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
# on charge le fond
background = pygame.image.load('assets/image.png')
# on veut que l'image de fond prenne toute la fenêtre
background = pygame.transform.scale(background, (window_height, window_width))

pygame.display.set_caption("Labyrinthe")
font = pygame.font.SysFont("Times New Roman, Arial", 40)

running = True
home = True
hard_mod = False
mod = pygame.image.load('assets/dark.png')
maze = None

while running:
    if home:
        screen.blit(background, (0, 0))
        screen.blit(play, play_rect)

        # on affiche des boutons pour modifier la longueur et la hauteur du labyrinthe
        up_width = pygame.transform.rotate(pygame.image.load('assets/haut.png'), 90)
        up_width_rect = up_width.get_rect()
        up_width_rect.x = 170
        up_width_rect.y = 20
        screen.blit(up_width, up_width_rect)

        txt_longueur = font.render('Longueur  :' + str(longueur), True, (0, 0, 0), (255, 255, 255))
        screen.blit(txt_longueur, (250, 40))

        down_width = pygame.transform.rotate(pygame.image.load('assets/haut.png'), 270)
        down_width_rect = down_width.get_rect()
        down_width_rect.x = 485
        down_width_rect.y = 20

        if longueur > 5:
            screen.blit(down_width, down_width_rect)

        up_height = pygame.transform.rotate(pygame.image.load('assets/haut.png'), 90)
        up_height_rect = up_height.get_rect()
        up_height_rect.x = 180
        up_height_rect.y = 100
        screen.blit(up_height, up_height_rect)

        txt_hauteur = font.render('Hauteur  :' + str(hauteur), True, (0, 0, 0), (255, 255, 255))
        screen.blit(txt_hauteur, (260, 120))

        down_height = pygame.transform.rotate(pygame.image.load('assets/haut.png'), 270)
        down_height_rect = down_height.get_rect()
        down_height_rect.x = 470
        down_height_rect.y = 100

        if hauteur > 5:
            screen.blit(down_height, down_height_rect)

        mod_button = pygame.transform.flip(pygame.image.load('assets/haut.png'), 0, 180)
        mod_button_rect = down_width.get_rect()
        mod_button_rect.x = 450
        mod_button_rect.y = 250
        screen.blit(mod_button, mod_button_rect)

        if hard_mod:
            ombre = "Oui"
        else:
            ombre = "Non"
        display_mod = font.render('Mode difficile : ' + ombre, True, (0, 0, 0), (255, 255, 255))
        screen.blit(display_mod, (200, 200))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                longueur = click(event, up_width_rect, longueur, 5)
                hauteur = click(event, up_height_rect, hauteur, 5)
                if longueur > 5:
                    longueur = click(event, down_width_rect, longueur, -5)
                if hauteur > 5:
                    hauteur = click(event, down_height_rect, hauteur, -5)
                if change_mod(event, mod_button_rect, hard_mod) is not None:
                    hard_mod = change_mod(event, mod_button_rect, hard_mod)
                if play_rect.collidepoint(event.pos) and not longueur == 0:
                    home = False
                    maze = Laby(longueur, longueur)
                    screen.fill((0, 0, 0))
            if event.type == pygame.QUIT:
                running = False
                home = False
    else:
        graphe = maze.graphe
        taille_case = window_height // longueur
        for noeud in graphe.get_noeuds():
            pygame.draw.circle(screen, (0, 255, 0),
                               ((noeud.get_x() + 1 / 2) * taille_case, (noeud.get_y() + 1 / 2) * taille_case), 30)
            # on dessine un arc entre chaque nœud et ses voisins
            for arc in noeud.get_arcs():
                pygame.draw.line(screen, (0, 255, 0),
                                 ((noeud.get_x() + 1 / 2) * taille_case, (noeud.get_y() + 1 / 2) * taille_case),
                                 ((arc.get_destination().get_x() + 1 / 2) * taille_case,
                                  (arc.get_destination().get_y() + 1 / 2) * taille_case),
                                 61)

        # on dessine le depart et l'arrivée
        pygame.draw.circle(screen, (255, 0, 0),
                           ((maze.depart.get_x() + 1 / 2) * taille_case, (maze.depart.get_y() + 1 / 2) * taille_case),
                           15)
        pygame.draw.circle(screen, (0, 0, 255),
                           ((maze.fin.get_x() + 1 / 2) * taille_case, (maze.fin.get_y() + 1 / 2) * taille_case), 15)

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                    debut = False
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_LEFT | pygame.K_q:
                            print("gauche")
                        case pygame.K_RIGHT | pygame.K_d:
                            print("droite")
                        case pygame.K_DOWN | pygame.K_s:
                            print("bas")
                        case pygame.K_UP | pygame.K_z:
                            print("haut")
                        case pygame.K_ESCAPE:
                            print(maze.solution)

    pygame.display.flip()

pygame.quit()
