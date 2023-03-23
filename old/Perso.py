import pygame


class Perso:
    def __init__(self, taille, debut):
        self.image = pygame.image.load('../assets/perso_old.png')
        self.rect = self.image.get_rect()
        self.taille_lab = int(taille)
        self.taille = int(10 / taille * 70)
        self.image = pygame.transform.scale(self.image, (self.taille, self.taille))
        self.position = debut

    def test_emplacement(self, lab, action):
        match action:
            case 'gauche':
                if self.position - 1 in lab[self.position - 1]:
                    self.rect.x -= self.taille
                    self.position -= 1
            case 'droite':
                if self.position + 1 in lab[self.position - 1]:
                    self.rect.x += self.taille
                    self.position += 1
            case 'haut':
                if self.position - self.taille_lab in lab[self.position - 1]:
                    self.rect.y -= self.taille
                    self.position -= self.taille_lab
            case 'bas':
                if self.position + self.taille_lab in lab[self.position - 1]:
                    self.rect.y += self.taille
                    self.position += self.taille_lab
