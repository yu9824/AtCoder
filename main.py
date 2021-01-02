def LI(): return list(map(int, input().split()))
def I(): return int(input())

import sys
sys.setrecursionlimit(10 ** 9)
from itertools import combinations


def main(*args):
    N, XY = args

    cnt = 0
    for (x1, y1), (x2, y2) in combinations(XY, 2):
        slope = (y2 - y1) / (x2 - x1)
        cnt += -1 <= slope <= 1
    print(cnt)


if __name__ == '__main__':
    N = int(input())
    args = [N]
    args.append([LI() for n in range(N)])
    main(*args)