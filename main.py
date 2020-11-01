# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)

from itertools import combinations

def main(*args):
    N, XY = args

    def difference(p1, p2):
        return p2[0] - p1[0], p2[1] - p1[1]

    for c in combinations(XY, r = 3):
        p1, p2, p3 = c  # p = (x, y)
        diff12 = difference(p1, p2)
        diff13 = difference(p1, p3)
        if diff12[1] * diff13[0] == diff13[1] * diff12[0]:
            print('Yes')
            break
    else:
        print('No')
    

if __name__ == '__main__':
    N = int(input())
    args = [N]
    args.append({tuple(map(int, input().split())) for n in range(N)})
    main(*args)
    