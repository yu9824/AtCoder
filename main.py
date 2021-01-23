def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)
from decimal import Decimal

def main(*args):
    N, X, VP = args
    s = Decimal(0)
    for i, (v, p) in enumerate(VP):
        s += Decimal(v) * Decimal(p) / Decimal(100)
        if s > X:
            print(i+1)
            break
    else:
        print(-1)

    

if __name__ == '__main__':
    N, X = LI()
    args = [N, X]
    args.append([LI() for n in range(N)])
    main(*args)