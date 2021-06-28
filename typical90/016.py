def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
# 思ったこと
O(N^2)でいける？

ローカルで実行している感じできる気がしなくて解説を見る．
解説: https://twitter.com/e869120/status/1383189464650981378

考え方はほとんど合っていた．
PyPy: 829 ms
Python: TLE

計算量計算でいけると思ったらPyPyで投げてみるのが吉なよう．
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_p


def main(*args):
    N, A, B, C = args
    A, B, C = sorted([A, B, C])
    
    LIM = 9999
    ans = LIM
    for j in range(LIM):
        for k in range(LIM-j+1):
            rest = N - (j*A + k*B)
            if rest % C == 0 and rest >= 0:
                l = rest // C
                ans = min(ans, j+k+l)
    print(ans)

    

if __name__ == '__main__':
    N = int(input())
    main(N, *LI())

