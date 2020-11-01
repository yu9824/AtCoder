
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


def cmb(n,r):
    from operator import mul
    from functools import reduce

    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under
