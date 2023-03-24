# Partie de Zhi-Sheng Trieu
import random
from Stack import *
from graphe.Graphe import Graphe


class Maze:
    def __init__(self, longueur: int, hauteur: int):
        self.t = longueur
        self.longueur = longueur
        self.hauteur = hauteur
        self.tab = []
        self.graphe = Graphe(self.longueur, self.hauteur)
        self.solution = []
        self.depart = self.graphe.depart
        self.fin = None
        # on crée les chemins
        self.dfs()

    def dfs(self):
        # on utilise le parcours en profondeur pour créer le labyrinthe
        visite = []  # cette liste permet de garder en mémoire les cases déjà visitées
        pile = Stack()
        pile.push(self.depart)
        while not pile.empty():
            u = pile.top()
            visite.append(u)
            u.visite()
            # récupère la liste des arcs possibles
            arcs = u.arcs_possibles(self.graphe)
            if arcs:
                # on choisit un arc au hasard dans la liste
                arc = random.choice(arcs)
                # on l'enlève de la liste des voisins possibles
                arcs.remove(arc)
                voisin = arc.get_destination()
                count = 1
                # on choisit un voisin au hasard et si ce voisin n'a pas été visité, on crée un arc entre les deux cases
                # sinon on en choisit un autre jusqu'à qu'on ait vu tous les voisins
                while voisin.visited and len(arcs):
                    arc = random.choice(arcs)
                    arcs.remove(arc)
                    voisin = arc.get_destination()
                    count += 1

                if not voisin.visited:
                    pile.push(voisin)
                    self.graphe.ajouter_arc(u, voisin)
                else:
                    # si on n'a pas de voisins non visités, c'est qu'on est arrivé à un cul-de-sac
                    # le premier cul-de-sac rencontré est la sortie
                    if not self.fin:
                        self.fin = u
                        self.solution = pile.data + [self.fin]
                    # on remonte dans la pile jusqu'à qu'on ait un voisin non visité
                    pile.pop()
