def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
# 思ったこと
星4以下を解く感じにしよう．


'''

# https://atcoder.jp/contests/typical90/tasks/typical90_j


def main(*args):
    N, CP, Q, LR = args
    

if __name__ == '__main__':
    N = int(input())
    CP = [LI() for n in range(N)]
    Q = int(input())
    LR = [LI() for q in range(Q)]
    main(N, CP, Q, LR)

