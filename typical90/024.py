def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと
K10**9だけど全探索で該当するものを選ぶってのはできるかな．

いや，普通に絶対値の引き算するだけで良いのでは？
それでdiff < Kかつ (K - diff) % 2 == 0 (打ち消し合う動作で無駄に回数を消費できる)だったらいける？
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_x

def main(*args):
    N, K, A, B = args
    diff = 0
    for a, b in zip(A, B):
        diff += abs(a-b) 
    if K > diff and (K - diff) % 2 == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main(*LI(), LI(), LI())
