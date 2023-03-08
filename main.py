from moteur import *
from laby import *
from button import *
from affichage import *

taille = 10  # on initialise la taille (longueur d'un coté) du labyrinthe carré à 10 qui pourra être modifiée dans le menu du jeu

pygame.init()
screen = pygame.display.set_mode((700, 700))  # on définit les dimensions de la fenêtre du jeu
background = pygame.image.load('assets/image.png')  # on charge les assets
background = pygame.transform.scale(background, (700, 700))
difficile = pygame.image.load('assets/dark.png')

pygame.display.set_caption("Labyrinthe")
font = pygame.font.SysFont("Times New Roman, Arial", 50)

running = True
debut = False
difficult = False

while running:

    screen.blit(background, (0, 0))
    screen.blit(play, play_rect)

    screen.blit(haut1, haut1_rect)

    if taille != 0:
        screen.blit(bas1, bas1_rect)

    screen.blit(bas2, bas2_rect)

    font_taille = font.render('Taille  :' + str(taille), True, (0, 0, 0), (255, 255, 255))
    screen.blit(font_taille, (200, 120))

    display_dificulty = font.render('Mode difficile  :' + str(difficult), True, (0, 0, 0), (255, 255, 255))
    screen.blit(display_dificulty, (200, 180))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:

            taille = click(event, haut1_rect, taille, 5)
            if not taille == 0:
                taille = click(event, bas1_rect, taille, -5)
            if diff(event, bas2_rect, difficult) is not None:
                difficult = diff(event, bas2_rect, difficult)
            if play_rect.collidepoint(event.pos) and not taille == 0:
                debut = True
                a = laby(taille)
                g = a.creation()
                moteur = Moteur(g, 0, taille ** 2 - 1, difficult)
                add(moteur.taille, moteur.matrice, moteur.liste_aff)
        if event.type == pygame.QUIT:
            running = False
            debut = False

    pygame.display.flip()

    while debut:
        moteur.liste_aff.draw(screen)
        screen.blit(moteur.depart.image, (moteur.depart.rect.x, moteur.depart.rect.y))
        screen.blit(moteur.arrive.image, (moteur.arrive.rect.x, moteur.arrive.rect.y))

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                    debut = False
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_LEFT | pygame.K_q:
                            moteur.perso.test_emplacement(moteur.matrice, 'gauche')
                        case pygame.K_RIGHT | pygame.K_d:
                            moteur.perso.test_emplacement(moteur.matrice, 'droite')
                        case pygame.K_DOWN | pygame.K_s:
                            moteur.perso.test_emplacement(moteur.matrice, 'bas')
                        case pygame.K_UP | pygame.K_z:
                            moteur.perso.test_emplacement(moteur.matrice, 'haut')
                        case pygame.K_ESCAPE:
                            print(a.solution(moteur.perso.emplacement, g))

        screen.blit(moteur.perso.image, moteur.perso.rect)

        if moteur.difficile:
            screen.blit(difficile, (moteur.perso.rect.x - 690, moteur.perso.rect.y - 690))

        if moteur.perso.emplacement == taille ** 2:
            running = False
            debut = False
            msg = font.render('You Win !', True, (255, 255, 255))
            # on veut que le message apparaisse au milieu de l'écran
            msg_rect = msg.get_rect(center=(350, 350))
            screen.blit(msg, msg_rect)

        pygame.display.flip()

        if not debut:
            pygame.time.wait(800)

pygame.quit()
