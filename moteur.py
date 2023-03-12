from Depart_arrive import Depart_arrive
from Perso import *


class Moteur:
    def __init__(self, matrice, depart, arrive, difficile):
        self.matrice = matrice
        self.taille = len(matrice) ** 0.5
        self.liste_aff = pygame.sprite.Group()
        self.depart = Depart_arrive(self.taille, (depart % self.taille, depart // self.taille), 'depart')
        self.arrive = Depart_arrive(self.taille, (arrive % self.taille, arrive // self.taille), 'arrive')
        self.perso = Perso(self.taille, depart + 1)
        self.difficile = difficile
