def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
# 思ったこと
浮動小数点だけ気をつければ大丈夫なのでは？
底はなんでもOK（両方同じ値なので）だから．

→通った
Python: 33 ms
PyPy: 106 ms

Decimalを使わないバージョンも調べたが，WAになった．

解説: https://twitter.com/e869120/status/1385001057512693762
浮動小数点が着目点というのは正解．
整数だけで処理しろ，というのが模範解答だった．
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_t

from decimal import Decimal
def main(*args):
    A, B, C = args
    if Decimal(A).log10() < B * Decimal(C).log10():
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main(*LI())

