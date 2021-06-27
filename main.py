def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
# 思ったこと

'''

# https://atcoder.jp/contests/typical90/tasks/typical90_l


def main(*args):
    H, W, Q, Query = args
    

if __name__ == '__main__':
    H, W = LI()
    Q = int(input())
    
    Query = [LI() for q in range(Q)]
    main(H, W, Q, Query)

