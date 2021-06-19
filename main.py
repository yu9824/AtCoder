def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
# 思ったこと
10**5なので，combinationをつかって総当たりは無理そう．
長さが平均になるように切れるようにするのが最適解な気がする． (L/(K+1))
後ろからと前からL/(K+1)より小さく切れるところで切っていった結果を比較すればいける？

いや．普通に差だけ比較すれば良いのでは？

わからないので回答を見る．https://twitter.com/e869120/status/1377027868518064129
# 答えで二分探索 がキーワード
「後ろからと前からL/(K+1)より小さく切れるところで切っていった結果を比較すればいける？」の考え方が惜しかった．この閾値を可変にして二分探索すればできた．
算数みたいに答えを直接答えを出すことにこだわってしまったが，そうとは限らないということか．
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_a

from math import ceil

def main(*args):
    N, L, K, A = args

    low = 0
    high = ceil(L / (K+1))

    while high - low > 1:
        mid = (low + high) // 2
        cnt = 0 # 何個切れ目を入れたかのカウント
        x = 0
        for i in range(N):
            if A[i] - x >= mid:
                cnt += 1
                x = A[i]
        if cnt >= K and L - x >= mid:   # 最後の最後も条件を満たしていれば 
            low = mid
        else:   # cnt < K
            high = mid
        print(high, low)
    print(mid)

            
                
            


if __name__ == '__main__':
    N, L = LI()
    K = int(input())
    A = LI()
    main(N, L, K, A)

