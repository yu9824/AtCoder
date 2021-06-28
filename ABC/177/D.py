# list(map(int, input().split()))
# int(input())

'''
参考
https://atcoder.jp/contests/abc177/editorial/90
https://atcoder.jp/contests/abc177/submissions/16407294
https://atcoder.jp/contests/atc001/tasks/unionfind_a
'''


from collections import Counter

# 再帰回数のエラー？と思われるので再帰上限を変更 10**3 → 10**9
# 変更したら RE がなくなったのでおそらくこれのせいで通らなかった
import sys
sys.setrecursionlimit(10 ** 9)

def main(N, M, C):
    lst = [n for n in range(N)] # 初期値はすべてがそれぞれ根である状態

    def get_root(x):    # 根を得る関数
        if lst[x] == x: # それ自身が根である場合
            return x
        else:   # 根が別のものである場合
            lst[x] = get_root(lst[x])   # 経路圧縮あり (ある種「メモ再帰化」)
            return lst[x]
            # return get_root(lst[x]) # 経路圧縮なし (わかりやすい，ただの再帰関数) → ちなみにこれだとTLEになってしまった．

    def unite(x, y):    # 集合の連結を行う関数
        root_x = get_root(x)
        root_y = get_root(y)
        if root_x != root_y:    # 根が違う (=異なる集合) ならば
            lst[root_x] = root_y

    {unite(*c) for c in C}  # 集合の連結を行う．
    print(max(Counter(map(get_root, lst)).values()))    # 一番大きい集合の大きさを得る．


if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    C = set()
    for _ in range(M):
        C.add(tuple(map(lambda x:int(x)-1, input().split())))   # pythonのindexに合わせるために "-1"
    main(N, M, C)
