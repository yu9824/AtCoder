def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
# 思ったこと
正直全然わかんないけどUnionFindみたいなイメージで繋がったらYesみたいにできたらなと思った．

ただ，全くわからず解答をみる．
解説: https://twitter.com/e869120/status/1380652465834532865
解答例: https://gitlab.com/w0mbat/kyopro_educational_90/-/blob/main/012.py

UnionFindなのはあっていたのがとてもうれしいが，二次元に対してどのように適用させるのかが本当に全くわからなかった．
2次元を1次元でuniqueに表すにはこういう表し方があるのだと勉強になった．

また，複雑な条件指定があり，典型がわかっても解けない自分の実力不足を感じた．
さらに，問題の読み違えもしており，読解力不足を感じた．

Python: 749 ms
PyPy: 403 ms
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_l


def main(*args):
    H, W, Q, Query = args

    uf = UnionFind(H*W)
    
    Color = [[False for w in range(W)] for h in range(H)]   # TrueがRed, FalseがWhite

    for q in range(Q):
        query = Query[q]
        if query[0] == 1:
            _, r, c = query
            r -= 1  # 1-index to 0-index
            c -= 1  # 1-index to 0-index
            Color[r][c] = True
            for i, j in _get_cand(r, c):
                if Color[i][j]:
                    uf.unite(r * W + c, i * W + j)
        elif query[0] == 2:
            _, ra, ca, rb, cb = map(lambda x:x-1, query)    # 1-index to 0-index
            n = ra * W + ca
            m = rb * W + cb
            if Color[ra][ca] and Color[rb][cb] and uf.is_same(n, m):    # 一個も塗られていない時にひっかからないように！
                print('Yes')
            else:
                print('No')

def _get_cand(i, j):
    for k, l in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        if 0 <= i + k < H and 0 <= j + l < W:
            yield (i+k, j+l)

class UnionFind:
    def __init__(self, N):
        '''
        N: 要素の数．
        '''
        self.root = list(range(N))

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

    def is_same(self, x, y):
        return self.get_root(x) == self.get_root(y)

    def get_groups(self):
        '''
        根をkey, 集合をvalueとしたgroupを返す．
        '''
        from collections import Counter
        return Counter(self.get_root(n) for n in range(len(self.root)))


if __name__ == '__main__':
    H, W = LI()
    Q = int(input())
    
    Query = [LI() for q in range(Q)]
    main(H, W, Q, Query)

