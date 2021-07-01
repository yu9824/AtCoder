def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと

'''

# https://atcoder.jp/contests/typical90/tasks/typical90_x

def main(*args):
    N, K, A, B = args
    print(N, K, A, B)

if __name__ == '__main__':
    main(*LI(), LI(), LI())
