# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)


def main(*args):
    N, A = args
    
    r = 0   # 通る最大座標．
    x = 0   # 一通りの操作がおわったときの　座標
    p = 0   # 合計の座標の変化
    q = 0   # 初期値が0として一通りの操作をやったときに通る最大座標
    for a in A:
        p += a
        q = max(q, p)
        r = max(r, x + q)
        x += p
    print(max(r, 0))

if __name__ == '__main__':
    N = int(input())
    args = [N]
    args.append(list(map(int, input().split())))
    main(*args)
