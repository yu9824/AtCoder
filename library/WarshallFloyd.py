

class WarshallFloyd:
    def __init__(self, graph, INF=2 ** 32):
        """graphには隣接行列を前提（コスト）

        Parameters
        ----------
        graph : 2D list
            Adjacency matrix representing an undirected graph.
            It takes the form of a square matrix with INF(2**32) being the place where there is no path.
        s : int, optional
            start node, by default 0
        INF : int, optional
            infinity
        """
        V = len(graph)
        self.INF = INF
        self.total_costs = graph

        for k in range(V):
            for s in range(V):
                for t in range(V):
                    self.total_costs[s][t] = min(self.total_costs[s][t], self.total_costs[s][k] + self.total_costs[k][t])