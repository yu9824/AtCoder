def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
# 思ったこと
星4以下を解く感じにしよう．

全くわからない．
貪欲になら解けるけど計算量的に絶対無理なのでさっさと答え見たほうが良さそう．

答えを見る．
解答: https://twitter.com/e869120/status/1379927227739987972

想像通り貪欲（全探索）ではO(N^7)の計算量が必要なので，どう考えても無理．（7はlen(atcoder)）

耳DP（状態DP）ってやつらしい．（***位置のほかに現在の状態をパラメータに持つことで解けるDP***）
由来は2019のEarsって問題の解法だったためらしい．https://atcoder.jp/contests/yahoo-procon2019-qual/tasks/yahoo_procon2019_qual_d

キーワード「状態DPによる高速化」
考え方が難しい
- 自分を採用する場合: 左上と横を受け継ぐ
- 自分を採用しない場合: 横だけ受け継ぐ
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_h


MOD = 10**9+7
def main(*args):
    N, S = args

    ATCODER = "atcoder"

    dp = [[0 for __ in range(N)] for _ in ATCODER]
    
    for n in range(N):
        for idx in range(len(ATCODER)):
            if S[n] == ATCODER[idx]:    # 採用可能な場合
                if idx == 0:    # 'a'だった場合
                    dp[idx][n] = 1
                elif n > 0: # idx > 0のとき，n > 0でしか厳密には採用できないので．
                    dp[idx][n] += (dp[idx-1][n-1] + dp[idx][n-1]) % MOD
            elif n > 0:   # 採用できない場合かつn > 0とき
                dp[idx][n] += dp[idx][n-1]

    print(dp)
        

if __name__ == '__main__':
    N = int(input())
    S = input()
    main(N, S)

