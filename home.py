import pygame

"""
script qui permet de gérer l'affichage de l'accueil
"""

up_width = pygame.transform.rotate(pygame.image.load('assets/haut.png'), 90)
up_width_rect = up_width.get_rect()
up_width_rect.x = 170
up_width_rect.y = 20

down_width = pygame.transform.rotate(pygame.image.load('assets/haut.png'), 270)
down_width_rect = down_width.get_rect()
down_width_rect.x = 485
down_width_rect.y = 20

up_height = pygame.transform.rotate(pygame.image.load('assets/haut.png'), 90)
up_height_rect = up_height.get_rect()
up_height_rect.x = 180
up_height_rect.y = 100

down_height = pygame.transform.rotate(pygame.image.load('assets/haut.png'), 270)
down_height_rect = down_height.get_rect()
down_height_rect.x = 470
down_height_rect.y = 100

mod_button = pygame.transform.rotate(pygame.image.load('assets/haut.png'), 270)
mod_button_rect = down_width.get_rect()
mod_button_rect.x = 510
mod_button_rect.y = 190

play = pygame.image.load("assets/play.png")
play = pygame.transform.scale(play, (100, 100))
play_rect = play.get_rect()
play_rect.x = 350 - play_rect.width // 2
play_rect.y = 350 - play_rect.height // 2


def click(event, objet, res, addition):
    if objet.collidepoint(event.pos):
        res += addition
    return res


def change_mod(event, objet, res):
    if objet.collidepoint(event.pos):
        return not res
