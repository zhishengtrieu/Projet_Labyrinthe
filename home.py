import pygame

"""
Classe qui permet de gérer l'affichage de l'accueil
"""


class Home:
    def __init__(self, screen, width, height, font):
        self.background = pygame.image.load("assets/laby.jpg")
        self.background = pygame.transform.scale(self.background, (width, height))
        self.screen = screen
        self.window_width = width
        self.window_height = height
        self.hard_mod = False
        self.font = font
        self.longueur, self.hauteur = 10, 10

        self.up_width = pygame.transform.rotate(pygame.image.load('assets/arrow.png'), 90)
        self.up_width_rect = self.up_width.get_rect()
        self.up_width_rect.x = width // 2 - self.up_width_rect.width // 2
        self.up_width_rect.y = 20

        self.down_width = pygame.transform.rotate(pygame.image.load('assets/arrow.png'), 270)
        self.down_width_rect = self.down_width.get_rect()
        self.down_width_rect.x = 485
        self.down_width_rect.y = 20

        self.up_height = pygame.transform.rotate(pygame.image.load('assets/arrow.png'), 90)
        self.up_height_rect = self.up_height.get_rect()
        self.up_height_rect.x = 180
        self.up_height_rect.y = 100

        self.down_height = pygame.transform.rotate(pygame.image.load('assets/arrow.png'), 270)
        self.down_height_rect = self.down_height.get_rect()
        self.down_height_rect.x = 470
        self.down_height_rect.y = 100

        self.mod_button = pygame.transform.rotate(pygame.image.load('assets/arrow.png'), 270)
        self.mod_button_rect = self.mod_button.get_rect()
        self.mod_button_rect.x = 510
        self.mod_button_rect.y = 190

        self.play = pygame.image.load("assets/play.png")
        self.play = pygame.transform.scale(self.play, (100, 100))
        self.play_rect = self.play.get_rect()
        self.play_rect.x = self.window_width // 2 - self.play_rect.width // 2
        self.play_rect.y = self.window_height // 2 - self.play_rect.height // 2

    def actualiser(self):
        self.screen.fill((0, 0, 0))
        # on affiche l'image de fond de l'accueil
        self.screen.blit(self.background, (0, 0))
        # on affiche des boutons pour modifier la longueur et la hauteur du labyrinthe
        self.screen.blit(self.up_width, self.up_width_rect)
        if self.longueur > 5:
            self.screen.blit(self.down_width, self.down_width_rect)
        self.screen.blit(self.up_height, self.up_height_rect)
        if self.hauteur > 5:
            self.screen.blit(self.down_height, self.down_height_rect)
        self.screen.blit(self.mod_button, self.mod_button_rect)
        # on affiche le bouton pour lancer le jeu
        self.screen.blit(self.play, self.play_rect)

        # on affiche le bouton pour changer le mode de difficulté
        if self.hard_mod:
            ombre = "Difficile"
        else:
            ombre = "Normal"
        display_mod = self.font.render('Mode : ' + ombre, True, (0, 0, 0), (255, 255, 255))
        self.screen.blit(display_mod, (250, 200))

        txt_longueur = self.font.render('Longueur  :' + str(self.longueur), True, (0, 0, 0), (255, 255, 255))
        self.screen.blit(txt_longueur, (250, 35))

    def click(self, event, objet, res, addition):
        if objet.collidepoint(event.pos):
            res += addition
        return res

    def change_mod(self, event, objet):
        if objet.collidepoint(event.pos):
            self.hard_mod = not self.hard_mod
