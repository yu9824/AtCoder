def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
# 思ったこと
累積和かなぁ．いもす法っぽい．
→TLEとれず．

累積和かな？→できた！
Python: 593 ms
PyPy: 439 ms

解説: https://twitter.com/e869120/status/1380652465834532865
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_j


def main(*args):
    N, CP, Q, LR = args
    ruiseki = [[0 for n in range(N+1)] for _ in range(2)]
    # 初期条件
    c1, p1 = CP[0]
    ruiseki[c1-1][1] = p1 # ruisekiは1-indexにしたほうが都合が良いので．
    for i in range(2, N+1): # 1-index
        c, p = CP[i-1]  # CPは0-index
        
        # 1-index to 0-index
        c -= 1

        ruiseki[c][i] = ruiseki[c][i-1] + p
        ruiseki[c^1][i] = ruiseki[c^1][i-1] # c^1で0と1を反転させてる
    
    {print(*[ruiseki[c][r] - ruiseki[c][l-1] for c in range(2)]) for l, r in LR}

if __name__ == '__main__':
    N = int(input())
    CP = [LI() for n in range(N)]
    Q = int(input())
    LR = [LI() for q in range(Q)]
    main(N, CP, Q, LR)

