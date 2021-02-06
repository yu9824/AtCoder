def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)


def main(*args):
    V, T, S, D = args
    if V * T <= D <= V * S:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    args = LI()
    main(*args)