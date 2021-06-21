
class UnionFind:
    def __init__(self, N):
        '''
        N: 要素の数．
        '''
        self.root = [n for n in range(N)]

    def get_root(self, x):
        '''
        x番目の根を取得．
        x: (0-index)
        '''
        if self.root[x] == x:
            return x
        else:
            self.root[x] = self.get_root(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        '''
        x番目の根とy番目の根を同じと紐づける．
        x: (0-index)
        y: (0-index)
        '''
        root_x = self.get_root(x)
        root_y = self.get_root(y)
        if root_x != root_y:
            self.root[root_x] = root_y

    def get_groups(self):
        '''
        根をkey, 集合をvalueとしたgroupを返す．
        '''
        from collections import Counter
        return Counter(self.get_root(n) for n in range(len(self.root)))


# 参考: https://qiita.com/takayg1/items/c811bd07c21923d7ec69
# 単位元 と 結合法則 (交換則は成り立たなくてOK) が必要! それらがあれば O(N)→O(log N) にできる．)
class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


def cmb(n,r):
    from operator import mul
    from functools import reduce

    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

def argsort(seq, reverse = False):
    # http://stackoverflow.com/questions/3071415/efficient-method-to-calculate-the-rank-vector-of-a-list-in-python
    # https://stackoverflow.com/questions/3382352/equivalent-of-numpy-argsort-in-basic-python
    return sorted(range(len(seq)), key=seq.__getitem__, reverse = reverse)

class Node:
    def __init__(self, node_id):
        self.parent = -1
        self.children = []
        self.depth = 0
        self.node_id = node_id
        self.c = 0

    def update(self, parent_node):
        self.depth = parent_node.depth + 1
        parent_node.children.append(self.node_id)
        self.parent = parent_node.node_id

# 隣接行列の場合
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
        N = len(graph)
        INF = 2**32
        self.total_costs = [INF for n in range(N)]
        
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

# 隣接リストの場合
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