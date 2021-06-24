def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
# 思ったこと
星4以下を解く感じにしよう．

O(N*Q)ならとけるけど制約条件的に無理そう．
二分探索がO(log(N))なので，O(log(N)*Q)にすればギリギリ解ける？

「最小値なので全探索？」という考えもある．

ひとりでに解けた．星3とはいえ，めちゃくちゃうれしい．
解き方もあってた．

計算量の見積もりだけ少し違った．
sort: O(N*log(N))
二分探索: O(log(N))
二分探索をBすべてで行うので全体の計算量は O(N*log(N)) + O(Q*log(N)) = O((N+Q)(log(N)))だった．

## 実行時間
PyPy: 603 ms(https://atcoder.jp/contests/typical90/submissions/23707992)
Python: 1583 ms(https://atcoder.jp/contests/typical90/submissions/23708073)

解答: https://twitter.com/e869120/status/1379565222541680644
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_g


def main(*args):
    N, A, Q, B = args
    A.sort()    # sort
    
    # 以下は典型的な二分探索構文
    for b in B:
        low = -1    # -1がミソ
        high = N    # Nがミソ
        while high - low > 1:
            mid = (low + high) // 2
            if b > A[mid]:
                low = mid
            else:
                high = mid
        if low == -1:   # それより小さい場合を拾えるかつindexerrorを防ぐ
            dissatisfaction = abs(b - A[high])
        elif high == N: # それより大きい場合を拾えるかつindexerrorを防ぐ
            dissatisfaction = abs(b - A[low])
        else:
            dissatisfaction = min(abs(b - A[high]), abs(b - A[low]))
        print(dissatisfaction)
    

if __name__ == '__main__':
    N = int(input())
    A = LI()
    Q = int(input())
    B = [int(input()) for q in range(Q)]
    main(N, A, Q, B)

