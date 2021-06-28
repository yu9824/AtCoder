def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
# 思ったこと

'''

# https://atcoder.jp/contests/typical90/tasks/typical90_r


def main(*args):
    T, L, X, Y, Q, E = args
    print(T, L, X, Y, Q, E)

if __name__ == '__main__':
    T = int(input())
    L, X, Y = LI()
    Q = int(input())
    E = [int(input()) for q in range(Q)]
    main(T, L, X, Y, Q, E)

