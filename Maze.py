# Partie de Zhi-Sheng Trieu
import random
from Stack import *
from Zoro import Zoro
from graphe.Graphe import Graphe
from Player import *


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
        self.dfs()
        self.player = Player(self.depart, self.taille_case)
        self.resolution()
        pos = random.choice(self.graphe.noeuds)
        self.zoro = Zoro(pos, self.taille_case)

    def dfs(self):
        """
        On utilise le parcours en profondeur pour créer le labyrinthe
        """

        pile = Stack()
        pile.push(self.depart)
        while not pile.empty():
            u = pile.top()
            u.visite()
            # récupère la liste des arcs possibles
            arcs = u.arcs_possibles(self.graphe)
            if arcs:
                # on choisit un arc au hasard dans la liste
                arc = random.choice(arcs)
                # on l'enlève de la liste des voisins possibles
                arcs.remove(arc)
                voisin = arc.get_destination()
                # on choisit un voisin au hasard et si ce voisin n'a pas été visité, on crée un arc entre les deux cases
                # sinon on en choisit un autre jusqu'à qu'on ait vu tous les voisins
                while voisin.visited and len(arcs):
                    arc = random.choice(arcs)
                    arcs.remove(arc)
                    voisin = arc.get_destination()

                if not voisin.visited:
                    pile.push(voisin)
                    self.graphe.ajouter_arc(u, voisin)
                else:
                    # si on n'a pas de voisins non visités, c'est qu'on est arrivé à un cul-de-sac
                    # on remonte dans la pile jusqu'à qu'on ait un voisin non visité
                    pile.pop()

    def resolution(self):
        """
        On utilise l'algorithme de Deep First Search pour trouver la solution
        """
        # on remet tous les nœuds à non visité
        for noeud in self.graphe.noeuds:
            noeud.visited = False
        # on utilise le parcours en profondeur pour créer le labyrinthe
        pile = Stack()
        pile.push(self.player.position)
        while not pile.empty():
            u = pile.top()

            if u == self.fin:
                self.solution = pile.data
                break
            u.visite()
            # récupère la liste des arcs
            arcs = u.get_arcs()
            for arc in arcs:
                voisin = arc.get_destination()
                if not voisin.visited:
                    pile.push(voisin)
                    break

            if voisin.visited:
                # si on n'a pas de voisins non visités, c'est qu'on est arrivé à un cul-de-sac,
                # on remonte dans la pile jusqu'à qu'on ait un voisin non visité
                pile.pop()
