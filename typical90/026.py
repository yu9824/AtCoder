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

計算量O(N)で解けるらしい．
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_z

def main(*args):
    N, AB = args
    # 隣接リスト
    graph = [[] for n in range(N)]
    for a, b in AB:
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

# 0, 1の二色で塗り分け．
# colors[x]がその色を表す
from collections import deque
cand = deque([0])
while cand:
    pos = cand.pop()
    colors[pos]
    


if __name__ == '__main__':
    N = int(input())
    main(N, {tuple(LI()) for n in range(N-1)})
