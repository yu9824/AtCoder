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
    graph = [[-1 for n in range(N)] for nn in range(N)]

    INF = 2 ** 32

    # graph[a][b]: a to b
    for a, b, c in ABC:
        graph[a-1][b-1] = c

    # for k in range(N):
    ans = 0
    for s in range(N):
        for t in range(N):
            threshold = INF
            rest = N
            while threshold >= 1:
                dijkstra = Dijkstra(graph, s, t, threshold)
                total_costs = dijkstra.total_costs
                try:
                    route = dijkstra.get_route(t)[1:-1]
                except:
                    pass
                if route:
                    threshold = max(route)
                else:
                    threshold = 0
                ans = ans + (total_costs[t] % INF) * (rest-threshold)
                rest -= threshold -2
                threshold -= 1
    print(ans)

class Dijkstra:
    def __init__(self, graph, s=0, g=0, threshold=None):
        """graphには隣接行列を前提（コスト）

        Parameters
        ----------
        graph : 2D list
            Adjacency matrix representing an undirected graph.
            It takes the form of a square matrix with -1 being the place where there is no path.
        s : int, optional
            start node, by default 0
        """
        import heapq
        N = len(graph)
        INF = 2**32
        self.total_costs = [INF for n in range(N)]
        threshold = 0 if threshold is None else threshold
        
        self.start_node = s
        self.d_route = {}

        que = []    # (total_cost, current_node)
        heapq.heappush(que, (0, self.start_node))
        self.total_costs[self.start_node] = 0

        while que:
            total_cost, current_node = heapq.heappop(que)
            for next_node, cost in enumerate(graph[current_node]):
                if cost < 0 :     # すでに訪れていた場合もしくはcostが0未満だった(辺がない)場合
                    continue
                if next_node > threshold and next_node != g:
                    continue
                # より少ないコストでそのノードにいける場合
                if self.total_costs[next_node] > total_cost + cost:
                    # コストを更新
                    self.total_costs[next_node] = total_cost + cost
                    # 最短距離を更新するノードの記録
                    self.d_route[next_node] = current_node  # ゴールから辿るため，この形．
                    # queに追加
                    heapq.heappush(que, (total_cost + cost, next_node))
        self.goal_node = current_node

    def get_radius(self, g):
        """[summary]

        Parameters
        ----------
        g : int
            goal node.
        """
        # 初期化
        r = 0
        previous_node = g
        while previous_node in self.d_route or previous_node != self.start_node:
            r += 1
            previous_node = self.d_route[previous_node]
        else:
            r += 1
        return r

    def get_route(self, g):
        """[summary]

        Parameters
        ----------
        g : int
            goal node.
        """
        route = []
        # 初期化
        previous_node = g
        while previous_node in self.d_route or previous_node != self.start_node:
            route.append(previous_node)
            previous_node = self.d_route[previous_node]
        else:
            route.append(previous_node)
        return route[::-1]



if __name__ == '__main__':
    N, M = LI()
    main(N, M, [LI() for m in range(M)])
