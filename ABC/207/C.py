def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
# 思ったこと
累積和かなぁ．いもす法っぽい．
→TLEとれず．

コンテスト終了後．
問題文の意味を取り間違えていた．最大個数重なっているときは何個なのかを聞かれているかと思ったが，単純に共通区間の数え上げだった．

閉区間，開区間をわかりやすく変換して数え上げして終わり．
> 2つの閉区間[a, b], [c, d]が共通部分を持つかの判定はmax(a, c) ≤ min(b, d)

imos法だと，O(N + 10**9)で無理なのには気づいたけど，問題文を読み違えていたからまずむずかしい．

PyPy: 346 ms
Python: 887 ms
'''

def main(*args):
    N, T, L, R = args
    for i in range(N):
        t = T[i]
        if t == 1:  # []
            pass
        elif t == 2:    # [)
            R[i] -= 0.5
        elif t == 3:    # (]
            L[i] += 0.5
        elif t == 4:    # ()
            R[i] -= 0.5
            L[i] += 0.5

    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if max(L[i], L[j]) <= min(R[i], R[j]):
                ans += 1
    print(ans)

    


if __name__ == '__main__':
    N = int(input())
    T = []
    L = []
    R = []
    for n in range(N):
        t, l, r = LI()
        T.append(t)
        L.append(l)
        R.append(r)
    main(N, T, L, R)

