def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと

'''

# https://atcoder.jp/contests/typical90/tasks/typical90_aq

def main(*args):
    H, W, rs, cs, rt, ct, S = args
    print(H, W, rs, cs, rt, ct, S)

if __name__ == '__main__':
    H, W = LI()
    rs, cs = LI()
    rt, ct = LI()
    main(H, W, rs, cs, rt, ct, [input() for h in range(H)])
