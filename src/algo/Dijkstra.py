from src.algo.Algorithme import Algorithme


class Dijkstra(Algorithme):
    """
    Algorithme de Dijkstra pour la recherche du plus court chemin
    """

    def __init__(self, graphe):
        self.graphe = graphe
        self.dist = {}
        self.prev = {}
        self.Q = set()
        self.S = set()
        self.path = []
        self.path_cost = 0

    def find_shortest_path(self, player):
        """
        On utilise l'algorithme de Dijkstra pour trouver la solution
        """
        self.dist = {}
        self.prev = {}
        self.Q = set()
        self.S = set()
        self.path = []
        self.path_cost = 0
        self.dist[player.position] = 0
        self.prev[player.position] = None
        self.Q.add(player.position)
        for noeud in self.graphe.noeuds:
            if noeud != player.position:
                self.dist[noeud] = float('inf')
                self.prev[noeud] = None
                self.Q.add(noeud)
        while self.Q:
            u = self.min_dist()
            self.S.add(u)
            self.Q.remove(u)
            for arc in u.get_arcs():
                v = arc.get_destination()
                if v not in self.S:
                    alt = self.dist[u] + 1
                    if alt < self.dist[v]:
                        self.dist[v] = alt
                        self.prev[v] = u
        self.path_cost = self.dist[self.graphe.fin]
        self.path = self.reconstruct_path()
        return self.path

    def reconstruct_path(self):
        """
        On reconstruit le chemin
        """
        res = []
        u = self.graphe.fin
        while u:
            res.append(u)
            u = self.prev[u]
        res.reverse()
        return res

    def min_dist(self):
        """
        On trouve le nœud avec la distance minimale
        """
        res = None
        min_dist = float('inf')
        for noeud in self.Q:
            if self.dist[noeud] < min_dist:
                min_dist = self.dist[noeud]
                res = noeud
        return res

    def generate(self):
        """
        On utilise l'algorithme de Dijkstra pour créer le labyrinthe
        TODO: A revoir
        """
        self.dist = {}
        self.prev = {}
        self.Q = set()
        self.S = set()
        self.path = []
        self.path_cost = 0
        self.dist[self.graphe.depart] = 0
        self.prev[self.graphe.depart] = None
        self.Q.add(self.graphe.depart)
        for noeud in self.graphe.noeuds:
            if noeud != self.graphe.depart:
                self.dist[noeud] = float('inf')
                self.prev[noeud] = None
                self.Q.add(noeud)
        while self.Q:
            u = self.min_dist()
            self.S.add(u)
            self.Q.remove(u)
            for arc in u.arcs_possibles(self.graphe):
                v = arc.get_destination()
                if v not in self.S:
                    alt = self.dist[u] + 1
                    if alt < self.dist[v]:
                        self.dist[v] = alt
                        self.prev[v] = u

        self.path_cost = self.dist[self.graphe.fin]
        self.path = self.reconstruct_path()
        return self.path

    def get_path(self):
        """
        On retourne le chemin
        """
        return self.path

