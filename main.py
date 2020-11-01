# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)

import numpy as np
from math import factorial
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

mod = 998244353

def main(*args):
    N, K, A = args

    tate = UnionFind(N)
    yoko = UnionFind(N)
    def solve(A, uf):
        for i in range(N):
            for j in range(0, i):
                if np.all((A[i] + A[j]) <= K):
                    uf.unite(i, j)
    solve(A, yoko)
    solve(A.T, tate)

    get_group = lambda uf: [element for element in Counter(uf.get_root(n) for n in range(N)).values() if element != 1]
    group_yoko = get_group(yoko)
    group_tate = get_group(tate)
    
    components =list(map(factorial, group_yoko + group_tate))
    
    ans = 1
    while components:
        ans *= components.pop(0) % mod
        ans %= mod
    print(ans)

if __name__ == '__main__':
    args = list(map(int, input().split()))
    N = args[0]
    A = np.array([list(map(int, input().split())) for n in range(N)])
    args.append(A)
    main(*args)



    