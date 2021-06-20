def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
# 思ったこと
前日のうちに値の受け取りの部分までやっておくと次の日やる気が起きやすい．
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_c



def main(*args):
    N, AB = args
    print(N, AB)
    

if __name__ == '__main__':
    N = int(input())
    AB = [LI() for _ in range(N-1)]
    main(N, AB)

