def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
# 思ったこと
前日のうちに値の受け取りの部分までやっておくと次の日やる気が起きやすい．

第一印象では，巡回セールス問題の亜種みたいなものなのかなと思った．
一本だけ引けるってことは循環しなくてもできる限り多い都市にいければ，勝手に元の都市に戻ることができるということ？
→Unionfind？
    →やってみたら全部くっついてしまって意味なかった．

通った: -1, 通れる: 1とかで幅優先探索とか？

求める道の本数も都市の数と一致する．（循環するため，m-1みたいな感じ）

わからないので解答をみる．
https://twitter.com/e869120/status/1377752658149175299

キーワード: 「木の直径は最短距離計算を2回やる」
木の直径→最短距離の最長距離

> 一本だけ引けるってことは循環しなくてもできる限り多い都市にいければ，勝手に元の都市に戻ることができるということ？
この考え方は正解だった．ただ，もう木構造の典型問題を知らないので解けなかった（DFS, BFSしか出てこなかったので計算量的に無理だなぁとしか思えなかった）

一番端っこの点を求める←これどうやるのかと考えていた．適当な番号を基準にしてしまうと計算がとても複雑だなと漠然と思っていた．
    とりあえず基準をおいて一番遠い点を求める．

無向グラフ→表し方が「隣接行列」もしくは，「隣接リスト」
    重みを持つ必要がないので隣接リスト？→隣接リストでも良かったが，今後のためを考えたダイクストラ法を実装したかったので隣接行列を使用．

Dijkstra法: 無向グラフで重みが非負のとき使える．貪欲法の一種．
ベルマンフォード法ってのもあるらしい．
参考: https://www.hongo.wide.ad.jp/~jo2lxq/dm/lecture/08.pdf
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_c



def main(*args):
    N, AB = args
    from collections import defaultdict
    # 隣接リスト
    graph = defaultdict(list)
    for a, b in AB:
        graph[a].append(b)
        graph[b].append(a)

    dijkstra = Dijkstra(graph, s=Dijkstra(graph=graph).goal_node)
    ans = dijkstra.get_radius(g=dijkstra.goal_node)
    print(ans)
    
    # 一番端っこにある点を求める→ダイクストラ法？

class Dijkstra:
    def __init__(self, graph, s=0):    
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
    AB = [map(lambda x:int(x)-1, input().split()) for _ in range(N-1)]
    main(N, AB)

