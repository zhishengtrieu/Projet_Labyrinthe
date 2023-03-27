from src.Maze import *
from src.Vues.Home import *
from src.perso.Player import *

# on initialise la longueur et la hauteur du labyrinthe


pygame.init()
# le screen est en plein écran
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# on charge le fond
background = pygame.image.load('assets/laby.jpg')
# on veut que l'image de fond prenne toute la fenêtre
window_width, window_height = pygame.display.get_window_size()

pygame.display.set_caption("Labyrinthe")
font = pygame.font.SysFont("Times New Roman, Arial", 40)

# on charge une icône pour la fenêtre
icon = pygame.image.load('assets/arrivee.png')
pygame.display.set_icon(icon)

running = True
home = True
maze = None
display_solution = False
end_game = False

accueil = Home(screen, window_width, window_height, font)

# on charge le bouton pour sortir du jeu ou revenir au menu
quit_button = pygame.image.load('assets/exit.png')
quit_button = pygame.transform.scale(quit_button, (80, 80))
quit_button_rect = quit_button.get_rect()
quit_button_rect.x = window_width - quit_button_rect.width - 10
quit_button_rect.y = 10

while running:
    if home:
        if end_game:
            end_game = False
        accueil.actualiser()

        # on met un contrôleur d'événement pour les boutons
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                accueil.longueur = accueil.click(event, accueil.up_width_rect, accueil.longueur, 1)
                accueil.hauteur = accueil.click(event, accueil.up_height_rect, accueil.hauteur, 1)
                if accueil.longueur > 5:
                    accueil.longueur = accueil.click(event, accueil.down_width_rect, accueil.longueur, -1)
                if accueil.hauteur > 5:
                    accueil.hauteur = accueil.click(event, accueil.down_height_rect, accueil.hauteur, -1)
                if accueil.change_mod(event, accueil.mod_button_rect) is not None:
                    accueil.change_mod(event, accueil.mod_button_rect)
                if accueil.play_rect.collidepoint(event.pos) and not accueil.longueur == 0:
                    home = False
                    case_height = window_height // accueil.hauteur
                    case_width = (window_width - 100) // accueil.longueur
                    taille_case = min(case_height, case_width)
                    maze = Maze(accueil.longueur, accueil.hauteur, taille_case)
                    player = maze.player
                # on ajoute le contrôleur d'événements pour le bouton
                if quit_button_rect.collidepoint(pygame.mouse.get_pos()):
                    if home:
                        running = False
                        home = False
            if event.type == pygame.QUIT:
                running = False
                home = False
    else:
        maze.actualiser(screen, taille_case, display_solution, accueil.hard_mod)

        # on affiche le message de victoire si le joueur arrive à la fin
        if player.position == maze.fin:
            home = True
            display_solution = False
            maze = None
            end_game = True

            msg = font.render('You Win !', True, (255, 0, 0))
            # on veut que le message apparaisse au milieu de l'écran
            msg_rect = msg.get_rect(center=(window_width // 2, window_height // 2))
            screen.blit(msg, msg_rect)

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                    debut = False
                case pygame.KEYDOWN:
                    maze.zoro.move()
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
                            maze.resolution()
                            display_solution = True
                case pygame.MOUSEBUTTONDOWN:
                    # on ajoute le contrôleur d'événements pour le bouton pour revenir à l'accueil
                    if quit_button_rect.collidepoint(pygame.mouse.get_pos()):
                        if not home:
                            home = True
                            display_solution = False
                            maze = None
                            break

        # on met un délai pour éviter que le jeu retourne instantanément à l'accueil
        if home and end_game:
            pygame.display.update()
            pygame.time.wait(800)

    screen.blit(quit_button, quit_button_rect)

    pygame.display.update()

pygame.quit()
