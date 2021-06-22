def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
# 思ったこと
星4以下を解く感じにしよう．
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_g

def main(*args):
    N, A, Q, B = args

    print(N, A, Q, B)
    

if __name__ == '__main__':
    N = int(input())
    A = LI()
    Q = int(input())
    B = [int(input()) for q in range(Q)]
    main(N, A, Q, B)

