def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

from math import ceil, floor, sqrt
from decimal import Decimal

def main(*args):
    X, Y, R = args
    x_low = ceil(X - R)
    x_high = floor(X + R)

    ans = 0
    f = lambda x: ((R ** 2 )- ((X - x) ** 2)).sqrt()
    for x in range(x_low, x_high+1):
        p = f(x)
        y_low = ceil(Y - p)
        y_high = floor(Y + p)
        ans += y_high - y_low + 1
    print(ans)    

if __name__ == '__main__':
    args = list(map(Decimal, input().split()))
    main(*args)
