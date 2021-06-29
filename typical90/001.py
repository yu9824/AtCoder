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

「最小値の最大化」は二分探索でとけることが多いそう．
O(N logL)
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_a
# 参考: https://qiita.com/kotaaaa/items/6d53d44c9ae11db10985

from math import ceil

def main(*args):
    N, L, K, A = args

    def boolean(mid):   # 指定通り切れた，もしくは指定以上に細かく切れた時はTrueを返す
        cnt = 0 # 何個切れ目を入れたかのカウント
        x = 0
        for a in A:
            if a - x >= mid and L - a >= mid:  # 今まで切った部品も，今切って残ってる部分も両方条件を満たすとき．
                cnt += 1    # 切る
                x = a   # 切れ目の更新
        return cnt >= K

    # 以下は典型的な二分探索構文
    low = 0
    high = ceil(L/(K+1)) + 1    # +1を忘れるとエラーになる．
    while high - low > 1:
        mid = (low + high) // 2
        if boolean(mid):
            low = mid
        else:
            high = mid
    print(low)  # ←ここがmidになってたのが間違えのもと


if __name__ == '__main__':
    N, L = LI()
    K = int(input())
    A = LI()
    main(N, L, K, A)

