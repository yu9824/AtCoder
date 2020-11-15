# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)

from decimal import Decimal

def main(*args):
    S = tuple(map(Decimal, args[:2]))
    G = tuple(map(Decimal, args[2:]))
    ans = (G[0] - S[0]) * S[1] / (G[1] + S[1]) + S[0]

    print('{:.7f}'.format(ans))

if __name__ == '__main__':
    args = list(map(int, input().split()))
    main(*args)
