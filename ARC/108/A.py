# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)

from math import ceil, floor
from decimal import Decimal

def main(*args):
    S, P = args
    r = Decimal(S ** 2 - 4 * P).sqrt()
    ans = (S + r) / Decimal(2), (S - r) / Decimal(2)
    # '{:.20f}'.format(ans[0])
    if floor(ans[0]) == ceil(ans[0]) and floor(ans[1]) == ceil(ans[1]):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    args = list(map(int, input().split()))
    main(*args)
