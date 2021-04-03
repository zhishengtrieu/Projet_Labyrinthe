import pygame

haut1 = pygame.image.load('assets/haut.png')
haut1_rect = haut1.get_rect()
haut1_rect.x = 130
haut1_rect.y = 110

haut2 = pygame.image.load('assets/haut.png')
haut2_rect = haut1.get_rect()
haut2_rect.x = 130
haut2_rect.y = 210

bas1 = pygame.transform.flip(pygame.image.load('assets/haut.png'), 0, 180)
bas1_rect = bas1.get_rect()
bas1_rect.x = 400
bas1_rect.y = 110

bas2 = pygame.transform.flip(pygame.image.load('assets/haut.png'), 0, 180)
bas2_rect = bas1.get_rect()
bas2_rect.x = 400
bas2_rect.y = 210

play = pygame.image.load("assets/start.png")
play_rect = play.get_rect()
play_rect.x = 350
play_rect.y = 400

def click (event, objet, res, addition):
    if objet.collidepoint(event.pos):
        res += addition
    return res

def diff (event, objet, res):
    if objet.collidepoint(event.pos):
        return not res