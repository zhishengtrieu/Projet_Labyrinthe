class Arc:
    def __init__(self, destination):
        self.destination = destination

    def get_destination(self):
        return self.destination


class Noeud:
    def __init__(self, x, y):
        self.arcs = []
        self.visited = False
        self.x = x
        self.y = y

    def ajouter_voisin(self, voisin):
        self.arcs.append(Arc(voisin))

    def voisins_possibles(self, graphe) -> list:
        # on récupère les voisins possibles qu'il y ait un chemin ou non
        voisins = []
        if self.x < graphe.longueur - 1:
            voisins.append(Arc(graphe.get_noeud(self.x + 1, self.y)))
        if self.x > 0:
            voisins.append(Arc(graphe.get_noeud(self.x - 1, self.y)))
        if self.y < graphe.hauteur - 1:
            voisins.append(Arc(graphe.get_noeud(self.x, self.y + 1)))
        if self.y > 0:
            voisins.append(Arc(graphe.get_noeud(self.x, self.y - 1)))
        return voisins

    def get_arcs(self) -> list:
        return self.arcs

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def visite(self):
        self.visited = True

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"({self.x}, {self.y})"




class Graphe:
    def __init__(self, longueur: int, hauteur: int):
        self.longueur = longueur
        self.hauteur = hauteur
        self.noeuds = []
        for j in range(self.hauteur):
            for i in range(self.longueur):
                self.noeuds.append(Noeud(i, j))
        self.depart = self.noeuds[0]
        self.fin = self.noeuds[-1]

    def get_noeuds(self) -> list:
        return self.noeuds

    def get_noeud(self, x: int, y: int) -> Noeud:
        return self.noeuds[x + y * self.longueur]

    def ajouter_arc(self, noeud1: Noeud, noeud2: Noeud):
        noeud1.ajouter_voisin(noeud2)
        noeud2.ajouter_voisin(noeud1)
