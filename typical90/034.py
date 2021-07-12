def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと
累積和みたいにやればいけるのでは？
配列のそれまでに出てきた種類と数を保存する．

連続する部分をひとまとまりにする？

REやTLEにはまったので解説を見た．
解説: https://twitter.com/e869120/status/1390798852299448322

考え方は合っていた．ただ自分のやろうとしている実装が複雑すぎるのでおかしいなとは思った．
尺取り法というらしい．

絶対増えること（単調増加）を生かして問題を解くらしい．

参考コード: https://github.com/hibit-at/typical90/blob/main/34.py
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_ah

from copy import copy
from collections import deque
def main(*args):
    N, K, A = args
    
    a = A[0]
    que = deque([a])
    ans = 0
    d = {}  # なぜこの辞書が必要なのか？

    n = 1
    while n < N:
        a = A[n]
        


        


if __name__ == '__main__':
    N, K = LI()
    main(N, K, LI())
