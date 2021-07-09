def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと

これグラフで，ダイクストラで求められるのでは？（なんとなく）
ダイクストラでは無理そう．（始点が決まっていないから）

N≤10だし普通に全探索？BFS?
見落としてたけど実行制限 5 secだった．

PyPy: 2341 ms
Python: 5513 ms

実装に20分くらいかかったけど解けた．
解説: https://twitter.com/e869120/status/1390074137192767489

permutationで全探索しようと思ったけどTLEっぽくてやめちゃった．計算量的に行けそうってのは理解していたけどなんか無理そうだった．
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_af

from collections import deque

def main(*args):
    N, A, M, XY = args

    INF = 2 ** 32

    NG = [set() for n in range(N)]
    for x, y in XY:
        NG[x-1].add(y-1)
        NG[y-1].add(x-1)
    
    ans = INF
    for s in range(N):  # スタート誰が走るか
        i = s   # 選手i
        j = 0   # 区間j
        que = deque([([i], A[i][j])])   # ([member1, member2, ...], cost)
        while que:
            members, cost = que.pop()
            if len(members) == N:
                ans = min(ans, cost)
            i = members[-1]
            for i_next in range(N):
                if i_next not in members and i_next not in NG[i]:   # まだ走っていないかつ直近の走者と喧嘩していない．
                    que.append((members + [i_next], cost + A[i_next][len(members)-1+1]))
    print(ans if ans != INF else -1)
        


    

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

class Dijkstra:
    def __init__(self, graph, s=0):
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
        V = len(graph)
        self.INF = 2**32
        self.total_costs = [self.INF for v in range(V)]
        
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
    N = int(input())
    A = [LI() for n in range(N)]
    M = int(input())
    main(N, A, M, [LI() for m in range(M)])
