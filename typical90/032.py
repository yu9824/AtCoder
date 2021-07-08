def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと

'''

# https://atcoder.jp/contests/typical90/tasks/typical90_af


def main(*args):
    N, A, M, XY = args

if __name__ == '__main__':
    N = int(input())
    A = [LI() for n in range(N)]
    M = int(input())
    main(N, A, M, [LI() for m in range(M)])
