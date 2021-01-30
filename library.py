
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

# 約数列挙
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

from math import ceil

def main(*args):
    N = args[0]

    ans = 0

    lst = make_divisors(N)
    for i in range(ceil(len(lst) / 2)):
        a = lst[i]
        b = lst[-1-i]
        if a % 2 or b % 2:
            ans += 2
    print(ans)

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

if __name__ == '__main__':
    args = [int(input())]

    main(*args)