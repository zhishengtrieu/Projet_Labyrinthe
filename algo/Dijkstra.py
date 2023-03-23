class Dijkstra:
    def __init__(self, graph):
        self.graph = graph
        self.dist = {}
        self.prev = {}
        self.Q = set()
        self.S = set()
        self.path = []
        self.path_cost = 0

    def find_shortest_path(self, start, end):
        self.dist[start] = 0
        self.Q.add(start)
        while self.Q:
            u = min(self.Q, key=lambda x: self.dist[x])
            self.Q.remove(u)
            self.S.add(u)
            if u == end:
                break
            for v in self.graph[u]:
                if v in self.S:
                    continue
                alt = self.dist[u] + self.graph[u][v]
                if v not in self.Q:
                    self.Q.add(v)
                elif alt >= self.dist[v]:
                    continue
                self.dist[v] = alt
                self.prev[v] = u
        self.path_cost = self.dist[end]
        self.path = self._reconstruct_path(start, end)
        return self.path, self.path_cost

    def _reconstruct_path(self, start, end):
        u = end
        path = []
        while u != start:
            path.append(u)
            u = self.prev[u]
        path.append(start)
        path.reverse()
        return path