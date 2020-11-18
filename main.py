# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)


# PyPyなら通った．
from copy import deepcopy
# もらうDP
mod = 10 ** 9 + 7

def main(*args):
    H, W, masu = args
    dp = [[0 for w in range(W)] for h in range(H)]
    hor = deepcopy(dp)  # horizontal「水平方向移動」のそこまでの累積和．hor[h][w] = dp[h][w-1] + dp[h][w-2] + ...
    ver = deepcopy(dp)  # vertical「垂直方向移動」のそこまでの累積和．ver[h][w] = dp[h-1][w] + dp[h-2][w] + ...
    dia = deepcopy(dp)  # diagonal「斜め方向移動」のそこまでの累積和．dia[h][w] = dp[h-1][w-1] + dp[h-2][w-2] + ...

    # 最初の位置は1通り
    dp[0][0] = 1
    for h in range(H):
        for w in range(W):  # 自分の位置を移動させてもらう．
            if masu[h][w]:   # 今いる自分の位置が移動可能な場所なら
                if w > 0 and masu[h][w-1]:   # 一マス上も移動可能な場所だったら
                    hor[h][w] += hor[h][w-1] + dp[h][w-1]   # (dp[h][w-2] + dp[h][w-3] + ...) + dp[h][w-1]
                    hor[h][w] %= mod
                if h > 0 and masu[h-1][w]:   # 一マス左も移動可能な場所だったら
                    ver[h][w] += ver[h-1][w] + dp[h-1][w]   # (dp[h-2][w] + dp[h-3][w] + ...) + dp[h-1][w]
                    ver[h][w] %= mod
                if h > 0 and w > 0 and masu[h-1][w-1]:   # 一マス左上も移動可能な場所だったら
                    dia[h][w] += dia[h-1][w-1] + dp[h-1][w-1]   # (dp[h-2][w-2] + dp[h-3][w-3] + ...) + dp[h-1][w-1]
                    dia[h][w] %= mod
                dp[h][w] += hor[h][w] + ver[h][w] + dia[h][w]
                dp[h][w] %= mod
    print(dp[-1][-1])

if __name__ == '__main__':
    H, W = list(map(int, input().split()))
    args = [H, W]
    args.append([[s == '.' for s in input()] for h in range(H)])
    main(*args)
