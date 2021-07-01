def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと
各辺がすべて最大公約数になるように切ればいいのでは？

Python: 34 ms
PyPy: 85 ms

解説: https://twitter.com/e869120/status/1385725481920520193
ユークリッドの互除法を学ぶためのものだった．最大公約数の考え方が合っていたのは嬉しい．
正直，何回やっても忘れちゃうし，Pythonには標準ライブラリで搭載されているので，忘れてしまいそう．．．

計算量がO(log(A+B+C))ってのは覚えておいたほうがいいかも．
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_v

from functools import reduce
from math import gcd
def main(*args):
    GCD = reduce(gcd, args)
    ans = 0
    for x in args:
        ans += x // GCD - 1 # たとえば2個に切るとき，1回切れば2個になる，という考え方
    print(ans)

if __name__ == '__main__':
    main(*LI())
