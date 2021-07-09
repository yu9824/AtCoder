def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと

'''

# https://atcoder.jp/contests/typical90/tasks/typical90_ag

def main(*args):
    H, W = args
    print(H, W)

if __name__ == '__main__':
    main(*LI())
