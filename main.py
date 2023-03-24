from Maze import *
from home import *
from Player import *

# on initialise la longueur et la hauteur du labyrinthe
longueur, hauteur = 10, 10

# la taille de la fenêtre du jeu
window_height, window_width = 700, 700

pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
# on charge le fond
background = pygame.image.load('assets/laby.jpg')
# on veut que l'image de fond prenne toute la fenêtre
background = pygame.transform.scale(background, (window_height, window_width))

pygame.display.set_caption("Labyrinthe")
font = pygame.font.SysFont("Times New Roman, Arial", 40)

running = True
home = True
hard_mod = False
mod = pygame.image.load('assets/dark.png')
maze = None
display_solution = False

while running:
    if home:
        # on affiche l'image de fond de l'accueil
        screen.blit(background, (0, 0))

        # on affiche des boutons pour modifier la longueur et la hauteur du labyrinthe
        screen.blit(up_width, up_width_rect)

        txt_longueur = font.render('Longueur  :' + str(longueur), True, (0, 0, 0), (255, 255, 255))
        screen.blit(txt_longueur, (250, 35))

        if longueur > 5:
            screen.blit(down_width, down_width_rect)

        screen.blit(up_height, up_height_rect)

        txt_hauteur = font.render('Hauteur  :' + str(hauteur), True, (0, 0, 0), (255, 255, 255))
        screen.blit(txt_hauteur, (260, 115))

        if hauteur > 5:
            screen.blit(down_height, down_height_rect)

        # on affiche le bouton pour changer le mode de difficulté
        if hard_mod:
            ombre = "Difficile"
        else:
            ombre = "Normal"
        display_mod = font.render('Mode : ' + ombre, True, (0, 0, 0), (255, 255, 255))
        screen.blit(display_mod, (250, 200))

        screen.blit(mod_button, mod_button_rect)

        # on affiche le bouton pour lancer le jeu
        screen.blit(play, play_rect)

        # on met un contrôleur d'événement pour les boutons
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
                    maze = Maze(longueur, hauteur)
                    taille_case = window_height // longueur
                    player = Player(maze.depart, taille_case)
                    screen.fill((0, 0, 0))
            if event.type == pygame.QUIT:
                running = False
                home = False
    else:
        graphe = maze.graphe
        for noeud in graphe.get_noeuds():
            pygame.draw.circle(screen, (255, 255, 255),
                               ((noeud.get_x() + 1 / 2) * taille_case, (noeud.get_y() + 1 / 2) * taille_case),
                               taille_case * 0.9 // 2)
            # on dessine un arc entre chaque nœud et ses voisins
            for arc in noeud.get_arcs():
                pygame.draw.line(screen, (255, 255, 255),
                                 ((noeud.get_x() + 1 / 2) * taille_case, (noeud.get_y() + 1 / 2) * taille_case),
                                 ((arc.get_destination().get_x() + 1 / 2) * taille_case,
                                  (arc.get_destination().get_y() + 1 / 2) * taille_case),
                                 int(taille_case * 0.9))

        if display_solution:
            # on affiche la solution
            for i in range(len(maze.solution) - 1):
                pygame.draw.line(screen, (255, 0, 0),
                                 ((maze.solution[i].get_x() + 1 / 2) * taille_case,
                                  (maze.solution[i].get_y() + 1 / 2) * taille_case),
                                 ((maze.solution[i + 1].get_x() + 1 / 2) * taille_case,
                                  (maze.solution[i + 1].get_y() + 1 / 2) * taille_case),
                                 taille_case // 2)
                # on dessine un cercle sur chaque nœud de la solution
                pygame.draw.circle(screen, (255, 0, 0),
                                   ((maze.solution[i].get_x() + 1 / 2) * taille_case,
                                    (maze.solution[i].get_y() + 1 / 2) * taille_case),
                                   taille_case // 4)

        # on affiche le depart et l'arrivée
        img_depart = pygame.image.load('assets/depart.png')
        img_depart = pygame.transform.scale(img_depart, (taille_case, taille_case))
        screen.blit(img_depart, (maze.depart.get_x() * taille_case, maze.depart.get_y() * taille_case))

        img_fin = pygame.image.load('assets/arrivee.png')
        img_fin = pygame.transform.scale(img_fin, (taille_case / 2, taille_case / 2))
        screen.blit(img_fin, ((maze.fin.get_x() + 1 / 4) * taille_case, (maze.fin.get_y() + 1 / 4) * taille_case))

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                    debut = False
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_LEFT | pygame.K_q:
                            player.move(maze, "gauche")
                        case pygame.K_RIGHT | pygame.K_d:
                            player.move(maze, "droite")
                        case pygame.K_DOWN | pygame.K_s:
                            player.move(maze, "bas")
                        case pygame.K_UP | pygame.K_z:
                            player.move(maze, "haut")
                        case pygame.K_ESCAPE:
                            display_solution = True

        # on affiche le joueur
        player.draw(screen)

        # on affiche l'ombre si le mode difficile est activé
        if hard_mod:
            player.draw_ombre(screen)

        # on affiche le message de victoire si le joueur arrive à la fin
        if player.position == maze.fin:
            running = False
            home = False
            msg = font.render('You Win !', True, (255, 0, 0))
            # on veut que le message apparaisse au milieu de l'écran
            msg_rect = msg.get_rect(center=(350, 350))
            screen.blit(msg, msg_rect)

    pygame.display.flip()

    # on met un délai pour éviter que le jeu se ferme instantanément
    if not running:
        pygame.time.wait(800)

pygame.quit()
