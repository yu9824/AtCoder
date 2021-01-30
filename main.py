def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

from math import ceil

def main(*args):
    N, S, D, XY = args
    for x, y in XY:
        if x < S and y > D:
            print('Yes')
            break
    else:
        print('No')

if __name__ == '__main__':
    N, S, D = LI()
    args = [N, S, D]
    args.append([LI() for n in range(N)])

    main(*args)