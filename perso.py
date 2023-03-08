import pygame


class Perso:
    def __init__(self, taille, debut):
        self.image = pygame.image.load('assets/perso.png')
        self.rect = self.image.get_rect()
        self.taille_lab = int(taille)
        self.taille = int(10 / taille * 70)
        self.image = pygame.transform.scale(self.image, (self.taille, self.taille))
        self.emplacement = debut

    def test_emplacement(self, lab, action):
        match action:
            case 'gauche':
                if self.emplacement - 1 in lab[self.emplacement - 1]:
                    self.rect.x -= self.taille
                    self.emplacement -= 1
            case 'droite':
                if self.emplacement + 1 in lab[self.emplacement - 1]:
                    self.rect.x += self.taille
                    self.emplacement += 1
            case 'haut':
                if self.emplacement - self.taille_lab in lab[self.emplacement - 1]:
                    self.rect.y -= self.taille
                    self.emplacement -= self.taille_lab
            case 'bas':
                if self.emplacement + self.taille_lab in lab[self.emplacement - 1]:
                    self.rect.y += self.taille
                    self.emplacement += self.taille_lab
