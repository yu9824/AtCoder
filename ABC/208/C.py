def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと

'''

# https://atcoder.jp/contests/abc208/tasks/abc208_c


from math import ceil, floor
def main(*args):
    N, K, A = args
    idx = argsort(A)
    
    amari = K % N
    if amari == 0:
        {print(K//N) for n in range(N)}
    else:
        # 浮動小数点で死んでたらしい．(ceil, floorによる処理のせい)
        c = K // N + 1
        f = K // N

        # ceil分配られるほう．
        upper = set(idx[:amari])
        for n in range(N):
            if n in upper:
                print(c)
            else:
                print(f)

def argsort(seq, reverse = False):
    # http://stackoverflow.com/questions/3071415/efficient-method-to-calculate-the-rank-vector-of-a-list-in-python
    # https://stackoverflow.com/questions/3382352/equivalent-of-numpy-argsort-in-basic-python
    return sorted(range(len(seq)), key=seq.__getitem__, reverse = reverse)


if __name__ == '__main__':
    main(*LI(), LI())
