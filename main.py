# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)

from collections import deque

'''
問題の肝: 木構造になるとき，絶対に良い書き込みができると気付けること．
→連結グラフなので絶対に全てが繋がった木構造が存在する．
→親を適当に決め，queでFIFOしながら親から子の順番で見てく
→根のラベルだけ適当に決め，親のラベルと辺のラベルが一致してれば子のラベルに適当な値を代入，一致していなければ子のラベルに辺のラベルの値を代入すればOK．
'''

class UnionFind:
    def __init__(self, N):
        self.root = [n for n in range(N)]

    def get_root(self, x):
        if self.root[x] == x:
            return x
        else:
            self.root[x] = self.get_root(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        root_x = self.get_root(x)
        root_y = self.get_root(y)
        if root_x != root_y:
            self.root[root_x] = root_y

    def get_groups(self):
        from collections import Counter
        return Counter(self.get_root(n) for n in range(len(self.root)))

def main(*args):
    N, M, G = args
    uf = UnionFind(N)
    
    graph = [[] for n in range(N)]  # それ自身のindex番号と0番目の値の頂点をつなぐ
    m = 0
    while m < M:
        u, v, c = G[m]
        if uf.get_root(u-1) != uf.get_root(v-1):
            uf.unite(u-1, v-1)
            graph[u-1].append([v-1, c])
            graph[v-1].append([u-1, c])
        m += 1

    visited = [False for n in range(N)]
    label = [-1 for n in range(N)]

    # 根を適当に決める．今回は0とする．
    visited[0] = True
    label[0] = 1    # ここのlabelはなんでもいいのでとりあえず1
    que = deque([0])  # 次訪れる場所をqueで管理
    while que:
        parent = que.popleft()
        for child, c in graph[parent]:
            if not visited[child]:  # 訪れていなければ (子供として成立していれば) (もし既に訪れていれば誰かの子供なのでこの親の子供ではない．)
                if label[parent] == c:  # 親のlabelと辺のラベルが一致しているならば
                    label[child] = 2 if c == 1 else 1   # なんか適当な値を入れる (辺のラベルが1じゃなければ適当に1を入れる．1のときは2をいれる)
                else:   # 親のlabelと辺のラベルが一致していないならば
                    label[child] = c
                visited[child] = True
                que.append(child)   # 次訪れる候補に追加
    {print(l) for l in label}


if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    args = [N, M] + [[list(map(int, input().split())) for m in range(M)]]
    main(*args)
    