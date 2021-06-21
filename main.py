def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
# 思ったこと

'''

# https://atcoder.jp/contests/typical90/tasks/typical90_d



def main(*args):
    H, W, A = args
    print(H, W, A)
    

if __name__ == '__main__':
    H, W = LI()
    A = [LI() for w in range(W)]
    main(H, W, A)

