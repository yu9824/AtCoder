def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと

'''

# https://atcoder.jp/contests/typical90/tasks/typical90_aa

def main(*args):
    N, S = args
    print(N, S)

if __name__ == '__main__':
    N = int(input())
    main(N, [input() for n in range(N)])
