def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと
累積和みたいにやればいけるのでは？
配列のそれまでに出てきた種類と数を保存する．

連続する部分をひとまとまりにする？

REやTLEにはまったので解説を見た．
解説: https://twitter.com/e869120/status/1390798852299448322

考え方は合っていた．ただ自分のやろうとしている実装が複雑すぎるのでおかしいなとは思った．
尺取り法というらしい．
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_ah

from copy import copy
from collections import deque
def main(*args):
    N, K, A = args
    
    loc = {a:[] for a in set(A)}
    l = 0   # その数字が続く一番左端
    a = A[l]
    a_previous = a
    que = deque([a])
    ans = 0

    n = 1
    while n < N:
        a = A[n]
        if a_previous != a:
            r = n
            loc[a_previous].append((l, r))
            l = n
            que.append(a)
            a_previous = a
        if len(set(que)) > K:
            al = que.popleft()  # 先頭が候補から消える
            l_first = loc[al][0][0]   # 一番最初にその数字が出てきた時の左端
            r_last = loc[al][-1][-1]  # 一番最後のその数字が出てきた右端 → 次はここからスタート
            loc[al] = []    # その数字のlocを初期化

            while al in que:
                loc[que.popleft()] = []    # その数字のlocを初期化
            ans = max(ans, r - l_first)
            n = r_last
        n += 1
    else:   # すべてのループが回った後，
        # 最後連続していた場合，それをloc辞書に追加できていないので，それを追加してあげる．（K==1の場合にバグるのを防ぐため）
        loc[a].append((l, n))
        l_first = loc[que.popleft()][0][0]
        ans = max(ans, n - l_first)

    print(ans)


        


if __name__ == '__main__':
    N, K = LI()
    main(N, K, LI())
