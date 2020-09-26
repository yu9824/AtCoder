# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)

from collections import Counter

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


    def final(self):
        for i in range(N):
            root_r = self.get_root(self.root[i])
            if root_r != self.root[i]:
                self.root[self.root[i]] = root_r

def main(N, M, AB):
    uf = UnionFind(N)
    {uf.unite(*ab) for ab in AB}
    c = Counter(map(uf.get_root, uf.root))
    print(len(c) - 1)

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    AB = {tuple(map(lambda x:int(x)-1, input().split())) for m in range(M)}
    main(N, M, AB)
