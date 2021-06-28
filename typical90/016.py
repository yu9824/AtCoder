def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
# 思ったこと

'''

# https://atcoder.jp/contests/typical90/tasks/typical90_p


def main(*args):
    N, A, B, C = args
    print(N, A, B, C)
    

if __name__ == '__main__':
    N = int(input())
    main(N, *LI())

