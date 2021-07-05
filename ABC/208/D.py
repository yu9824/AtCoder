def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと
有向グラフってやつでしょうか？
隣接行列？
N ≤ 400だから普通に全探索やればいける？

経路問題の本質を理解していればできたらしい．
ついでに他の経路問題もlibrary.pyに足してみようかな．
'''

def main(*args):
    N, M, ABC = args
    INF = 2 ** 32
    graph = [[INF for n in range(N)] for nn in range(N)]

    # graph[a][b]: a to b
    for a, b, c in ABC:
        graph[a-1][b-1] = c

    ans = 0
    print(WarshallFloyd(graph).graph)

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
        self.graph = graph
        V = len(self.graph)
        self.INF = INF
        self.total_costs = [self.INF for v in range(V)]

        for k in range(V):
            for s in range(V):
                for t in range(V):
                    self.graph[s][t] = min(graph[s][t], graph[s][k] + graph[k][t])



if __name__ == '__main__':
    N, M = LI()
    main(N, M, [LI() for m in range(M)])
