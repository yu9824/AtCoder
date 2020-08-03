# list(map(int, input().split()))
# int(input())

from math import ceil
# 小数点以下を繰り上げた値を出力するので，最大長さを整数の中 (0からmax(A)の間) から探す． (これをxとする)
# すべての本数をxより小さくするまでの回数がK以下であれば良い．

def main(N, K, A):
    # 二分探索内で用いる判定用関数
    def check(x):   # すべての長さをx以下にするための回数
        cnt = 0 # すべての長さをx以下にするために何回切ったか
        for a in A:
            cnt += ceil(a / x) - 1  # 切り口は1つ少ない
        return cnt <= K # K回以内で操作を終えることができたかどうか．

    l, r = 0, max(A)    # この中をxが動く．
    while l < r - 1:    # 差が1未満 == lとrが隣り合わせ == rができる最小， lができない最大を示し，それらが隣り合わせ
        mid = (l + r) // 2
        if check(mid): # 真ん中の条件でも終えることができるならそれよりも小さくできるので， r (最大方向) を縮める．
            r = mid
        else:
            l = mid
    print(r)


if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    main(N, K, A)
