"""
Classe easter egg pour le personnage de Roronoa Zoro.
Il est perdu dans un labyrinthe et marche au hasard
"""
import random

import pygame

from src.perso.Player import Player


class Zoro(Player):
    def __init__(self, noeud, taille):
        super().__init__(noeud, taille)
        self.image = pygame.transform.scale(pygame.image.load("assets/zoro.png"), (self.taille, self.taille))

    def move(self):
        """
        Zoro se déplace au hasard
        """
        arcs = self.position.get_arcs()
        arc = random.choice(arcs)
        self.position = arc.destination
        self.rect.x = self.position.x * self.taille
        self.rect.y = self.position.y * self.taille
