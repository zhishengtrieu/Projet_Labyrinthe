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

    def arcs_possibles(self, graphe) -> list:
        # on récupère les voisins possibles qu'il y ait un chemin ou non
        arcs = []
        if self.x < graphe.longueur - 1:
            arcs.append(Arc(self.voisin("droite", graphe)))
        if self.x > 0:
            arcs.append(Arc(self.voisin("gauche", graphe)))
        if self.y < graphe.hauteur - 1:
            arcs.append(Arc(self.voisin("bas", graphe)))
        if self.y > 0:
            arcs.append(Arc(self.voisin("haut", graphe)))
        return arcs

    def voisin(self, direction, graphe):
        match direction:
            case "droite":
                return graphe.get_noeud(self.x + 1, self.y)
            case "gauche":
                return graphe.get_noeud(self.x - 1, self.y)
            case "bas":
                return graphe.get_noeud(self.x, self.y + 1)
            case "haut":
                return graphe.get_noeud(self.x, self.y - 1)

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
