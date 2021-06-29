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

全然実装できなかったが，勘違いしている点があった．
- dp[pos][atcoderの何文字目まで] = 通り数
    - このとき，0 ~ len(ATCODER)で，0は0-indexの0ではなく，1-indexの0である．つまり，まだ何も選んでいない状態は何通りか, i.e. 1通りと考えることができる．
    - そのため，dp.shape(N+1, len(ATCODER)+1)
- 全部 += だと思ってたら必ずしもそうしなくてもよかったっぽい．

最終的な参考回答: https://qiita.com/toast-uz/items/bf6f142bace86c525532#44-%E8%80%B3dp
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_h

MOD = 10**9+7

def main(*args):
    N, S = args

    ATCODER = "atcoder"
    dp = [[0 for __ in ' ' + ATCODER] for _ in range(N+1)]
    
    for i in range(N+1):
        for j in range(len(ATCODER)+1):
            if j == 0:
                dp[i][j] = 1
            elif i == 0:
                pass    # 初期値が0なので．
            elif S[i-1] == ATCODER[j-1]:
                dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % MOD
            else:
                dp[i][j] = dp[i-1][j]
    
    # 回答に載ってる図のような形で出力
    # import pandas as pd; print(pd.DataFrame(dp, columns = list(' ' + ATCODER), index = list(S+' ')).transpose())
    print(dp[-1][-1])

if __name__ == '__main__':
    N = int(input())
    S = input()
    main(N, S)

