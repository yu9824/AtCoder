def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと
確実に解けるのは長方形の範囲内に重なったら+1をする動作だけど，これだと(10**3)**2 * 10**5なので現実的ではない．
累積和とかできたら面白いのになとは思ったりする．

逆にN枚のうちからk枚のペアを選んで，重なり合う部分を考えるとかも愚直にできそうだけど，これも計算量およびk枚だけしか重なっていないことの保証が難しそう．
すべて長方形なはずだから長方形単位で考える→重なる場合は分割してそれぞれに重なった数を持たせる？

わからないので早々にGive up．
解説: https://twitter.com/e869120/status/1388262816101007363

> 累積和とかできたら面白いのになとは思ったりする．
なぜか当たっていて，imos法だった．imos法は何回かやったことあるけど二次元はやったことがないのでいい機会がなので原著サイトを見ながら実装してみよう．
よく考えるとなぜか当たったというよりはimos法のサイトは何度かみているので，なんとなく見覚えがあったのかもしれない．

imos法原著サイト: https://imoz.jp/algorithms/imos_method.html
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_ab

def main(*args):
    N, lst = args
    H = 1000
    W = 1000

    # 二次元の累積和用
    tiles = [[0 for _ in range(W+1)] for __ in range(H+1)]  # 最後の-1がはみ出る可能性があるから．
    for n in range(N):
        lx, ly, rx, ry = map(lambda x:x-1, lst[n])  # 1-index to 0-index
        # 対角線で和差を揃える．
        tiles[ly][lx] += 1
        tiles[ry][lx] -= 1
        tiles[ly][rx] -= 1
        tiles[ry][rx] += 1

    # 横方向の累積和
    for h in range(H):
        for w in range(1, W):
            tiles[h][w] += tiles[h][w-1]
    
    # 縦方向の累積和
    for h in range(1, H):
        for w in range(W):
            tiles[h][w] += tiles[h-1][w]

    # answer
    counta = [0 for n in range(N+1)]
    for h in range(H):
        for w in range(W):
            counta[tiles[h][w]] += 1
    [print(counta[n]) for n in range(1, N+1)]



if __name__ == '__main__':
    N = int(input())
    main(N, [LI() for n in range(N)])
