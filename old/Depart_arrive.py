import pygame


class Depart_arrive:
    def __init__(self, taille, empl, img):
        self.taille = int(10 / taille * 70)
        self.image = pygame.image.load('../assets/' + img + '.png')
        self.image = pygame.transform.scale(self.image, (self.taille // 2, self.taille // 2))
        self.rect = self.image.get_rect()
        self.rect.x = self.taille * empl[0] + self.taille // 4
        self.rect.y = self.taille * empl[1]
