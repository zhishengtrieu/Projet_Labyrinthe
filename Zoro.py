"""
Classe easter egg pour le personnage de Roronoa Zoro.
Il est perdu dans un labyrinthe et marche au hasard
"""
import pygame

from Player import Player


class Zoro(Player):
    def __init__(self, noeud, taille):
        super().__init__(noeud, taille)
        self.image = pygame.transform.scale(pygame.image.load("assets/zoro.png"), (self.taille, self.taille))
