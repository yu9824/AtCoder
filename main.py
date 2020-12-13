# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)


def cmb(n,r):
    from operator import mul
    from functools import reduce

    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

def main(*args):
    L = args[0]
    print(cmb(L-1, 11))
    

if __name__ == '__main__':
    args = [int(input())]
    main(*args)