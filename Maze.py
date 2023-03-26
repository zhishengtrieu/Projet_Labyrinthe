# Partie de Zhi-Sheng Trieu
import random
from Stack import *
from Zoro import Zoro
from graphe.Graphe import Graphe
from Player import *
from algo.DFS import DFS
from algo.Dijkstra import Dijkstra


class Maze:
    """
    Classe qui gère le labyrinthe
    """

    def __init__(self, longueur: int, hauteur: int, taille_case: int):
        self.solution = []
        self.longueur = longueur
        self.hauteur = hauteur
        self.taille_case = taille_case
        self.graphe = Graphe(self.longueur, self.hauteur)
        self.depart = self.graphe.depart
        self.fin = self.graphe.fin
        # on crée les chemins
        self.algo = DFS(self.graphe)
        self.algo.generate()
        self.player = Player(self.depart, self.taille_case)
        self.resolution()
        pos = random.choice(self.graphe.noeuds)
        self.zoro = Zoro(pos, self.taille_case)

    def resolution(self):
        """
        On résout le labyrinthe
        """
        self.solution = self.algo.find_shortest_path(self.player)
