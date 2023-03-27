from src.algo.Algorithme import Algorithme


class BellmanFord(Algorithme):
    """
    Algorithme de Bellman-Ford pour la recherche du plus court chemin
    """

    def __init__(self, graphe):
        self.graphe = graphe
        self.dist = {}
        self.prev = {}
        self.path = []
        self.path_cost = 0

    def find_shortest_path(self, player):
        """
        On utilise l'algorithme de Bellman-Ford pour trouver la solution
        """
        self.dist = {}
        self.prev = {}
        self.path = []
        self.path_cost = 0
        self.dist[player.position] = 0
        self.prev[player.position] = None
        # on initialise les distances
        for noeud in self.graphe.noeuds:
            if noeud != player.position:
                self.dist[noeud] = float('inf')
                self.prev[noeud] = None

        changement = True
        while changement:
            changement = False
            for noeud in self.graphe.noeuds:
                for arc in noeud.get_arcs():
                    v = arc.get_destination()
                    alt = self.dist[noeud] + 1
                    if alt < self.dist[v]:
                        self.dist[v] = alt
                        self.prev[v] = noeud
                        changement = True

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
