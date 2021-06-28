# list(map(int, input().split()))
# int(input())

mod = 998244353

# 貰うDP
# Pythonで普通に通った．
# Aのような累積， のようなものを使って復元して高速化するケースはよくあるらしい．
def main(N, S):
    dp = [0 if n != 0 else 1 for n in range(N)]     # dp[i]はマスiに行く通り数． (答えはdp[-1]), dp[0] = 1 (最初にいる場所だから1通り)
    A = [0 if n != 0 else 1 for n in range(N)]      # dp[i] = A[i] - A[i-1] (i >= 1), A[0] = dp[0] = 1 (i = 0) が成り立つような配列を考える． (累積を取っておく配列)

    for i in range(1, N):   # 今いる点 (注目点)
        for l, r in S:  # 選択行動範囲 (l: 始点, r: 終点)
            if i - l < 0:   # 注目点が選択行動範囲の始点より手前の場合 → 注目点に来るために使用することはできない．
                break
            else:           # 注目点に来るために使用することができる場合
                if i - r <= 0:  # lからrの間で，注目点に行くために使用できる点を逆算． そこに行くことができる = 選択行動範囲の値を選択することで注目点に達することができる通り数．
                    dp[i] += A[i-l]
                else:
                    dp[i] += A[i-l] - A[i-r-1]
        dp[i] %= mod
        A[i] = (A[i-1] + dp[i]) % mod
    print(dp[-1])

if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    S = {tuple(map(int, input().split())) for k in range(K)}
    S = sorted(list(S), key = lambda x:x[0])    # 始点でsort (範囲の重複がないため)
    main(N, S)


'''
# 配るDP

# PyPyでもPythonでもTLE → ただのDPでは間に合わない？(最大O(N^2)だから？)
def main(N, S):
    dp = [0 if n != 0 else 1 for n in range(N)] # 初期値
    lst_S = sorted(list(S))

    for i in range(N):
        if dp[i] == 0:  # 計算時間削減のため， 時間さえ間に合えば不要かも．
            continue
        for j in lst_S: # このfor文内で同じものを足す機会が多い→これを削減？
            if i + j > N - 1:
                break
            else:
                dp[i+j] = (dp[i+j] + dp[i]) % mod
    print(dp[-1])


if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    S = set()
    for k in range(K):
        L, R = map(int, input().split())
        {S.add(i) for i in range(L, R+1)}
    main(N, S)
'''
