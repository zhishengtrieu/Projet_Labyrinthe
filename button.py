import pygame

up_width = pygame.image.load('assets/haut.png')
up_width_rect = up_width.get_rect()
up_width_rect.x = 20
up_width_rect.y = 20

down_width = pygame.transform.flip(pygame.image.load('assets/haut.png'), 0, 180)
down_width_rect = down_width.get_rect()
down_width_rect.x = 350
down_width_rect.y = 20

haut2 = pygame.image.load('assets/haut.png')
haut2_rect = up_width.get_rect()
haut2_rect.x = 130
haut2_rect.y = 210

bas2 = pygame.transform.flip(pygame.image.load('assets/haut.png'), 0, 180)
bas2_rect = down_width.get_rect()
bas2_rect.x = 400
bas2_rect.y = 250

play = pygame.image.load("assets/start.png")
play = pygame.transform.scale(play, (100, 100))
play_rect = play.get_rect()
play_rect.x = 350 - play_rect.width // 2
play_rect.y = 350 - play_rect.height // 2


def click(event, objet, res, addition):
    if objet.collidepoint(event.pos):
        res += addition
    return res


def diff(event, objet, res):
    if objet.collidepoint(event.pos):
        return not res
