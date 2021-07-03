def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと

'''

# https://atcoder.jp/contests/typical90/tasks/typical90_z

def main(*args):
    N, AB = args
    print(N, AB)

if __name__ == '__main__':
    N = int(input())
    main(N, {tuple(LI()) for n in range(N-1)})
