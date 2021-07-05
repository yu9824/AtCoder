'''
Dijkstraと違って，-1を道のない場合としてはいけない（負の場合も対応してしまっているため，-1のコストを持つ辺であると認識されてしまう．
そこでINF = 2 ** 32と定義して，それにより初期化することとする．それが入力されている辺は道がないとして除外する．
'''


# 隣接行列の場合
class BellmanFord:
    def __init__(self, graph, s=0, INF=2**32):
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
        self.total_costs = [self.INF for v in range(V)]
        
        self.start_node = s
        self.d_route = {}
        self.total_costs[self.start_node] = 0

        from collections import deque
        que = deque([(0, self.start_node, 0)])  # (total_cost, current_node, how_many_nodes)
        while que:
            total_cost, current_node, how_many_nodes = que.pop()
            # もしV-1回より多く推移を繰り返している場合（何個のnodeに訪問したか？）
            if how_many_nodes > V-1:
                continue
            for next_node, cost in enumerate(graph[current_node]):
                # 道がない場合
                if cost == self.INF:
                    continue
                # より少ないコストでそのノードにいける場合
                if self.total_costs[next_node] > total_cost + cost:
                    # コストを更新
                    self.total_costs[next_node] = total_cost + cost
                    # 最短距離を更新するノードの記録
                    self.d_route[next_node] = current_node  # ゴールから辿るため，この形．
                    # queに追加
                    que.append((total_cost + cost, next_node, how_many_nodes + 1))
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
    INF = 2 ** 32
    print(BellmanFord([[INF, INF, 2], [0, INF, 4], [INF, 5, INF]]).total_costs)