def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと

UnionFindではできないな．
木の取り扱いは隣接行列と隣接リストしか知らないけど，とりあえずそれでやってみよう．

木の直径が2以上な組み合わせを探せばいいのでは？

全くわからないので解説を見る．
解説: https://twitter.com/e869120/status/1387175538544975872

「二部グラフの性質を使おう」そもそも二部グラフを知らない．
二部グラフ
- 奇数長の閉路を含まない．
- 最大マッチングが多項式時間で計算できる．←さっぱりわからない．

木は必ず二部グラフなので，という考え方らしい．
そもそも問題文を二色の彩色問題に読み替えることが自分にはできないので解説をすぐみて正解．

正直そもそも解けるようになる気もあまりしない．
二部グラフについて: https://ocw.hokudai.ac.jp/wp-content/uploads/2016/01/GraphTheory-2007-Note-03.pdf
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_z

def main(*args):
    N, AB = args
    # 隣接リスト
    lst = [[] for n in range(N)]
    for a, b in AB:
        a -= 1
        b -= 1
        lst[a].append(b)
        lst[b].append(a)
    dijkstra = Dijkstra(lst)
    print(dijkstra.goal_node)

class Dijkstra:
    def __init__(self, graph, s=0):
        """graphには隣接リストを前提（コスト）

        Parameters
        ----------
        graph : 2D list
            Adjacent list representing an undirected graph.
        s : int, optional
            start node, by default 0
        """
        import heapq
        N = len(graph)
        INF = 2**32
        cost = 1
        
        self.total_costs = [INF for n in range(N)]
        
        self.start_node = s
        self.d_route = {}

        que = []    # (total_cost, current_node)
        heapq.heappush(que, (0, self.start_node))
        self.total_costs[self.start_node] = 0

        while que:
            total_cost, current_node = heapq.heappop(que)
            for next_node in graph[current_node]:
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
    main(N, {tuple(LI()) for n in range(N-1)})
