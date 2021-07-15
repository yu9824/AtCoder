def LI(): return list(map(int, input().split()))

INF = 2 ** 32 - 1

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと
DP?

なんの情報を持たせるべきか？
- これまで曲がった回数
- これまでどういう方向で進んできたか．
- 今回はどう進む関係なのか．

渡すDPを書いたがTLE & WA
PyPy: 17AC 6WA 5TLE

限界なので，解説を見る．
解説: https://twitter.com/e869120/status/1394787605099601923

popleftを使ったりしていて，BFSなのは正解でそれはよかった．（最短経路はBFSって感じらしい．）
自分のやつのどこが重たいのか，どこが間違っているのかはわからない．

dpに方向性という概念を与えてあげるとよかったらしい．
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_aq

from collections import deque

def main(*args):
    H, W, rs, cs, rt, ct, S = args

    lst_direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
    dp = [[[INF] * len(lst_direction) for w in range(W)] for h in range(H)] # 方向という概念を持たせる．

    OK = '.'
    NG = '#'

    def get_candidate(x, y, direction):
        dx, dy = lst_direction[direction]
        x_cand = x + dx
        y_cand = y + dy
        return x_cand, y_cand

    def is_available(x, y):
        return 0 <= x < H and 0 <= y < W and S[x][y] == OK

    # 初期化
    que = deque()
    for direction in range(len(lst_direction)):
        dp[rs][cs][direction] = 0
        que.append([(rs, cs), direction])

    while que:
        (x, y), direction = que.popleft()
        x_cand, y_cand = get_candidate(x, y, direction)
        if is_available(x_cand, y_cand):
            cost_cand = dp[x_cand][y_cand][direction]
            cost = dp[x][y][direction]
            if cost <= cost_cand:
                dp[x_cand][y_cand][direction] = cost
                for direction_cand in range(len(lst_direction)):
                    if direction_cand != direction:
                        dp[x_cand][y_cand][direction_cand] = cost + 1
                    que.append([(x_cand, y_cand), direction_cand])
    print(min(dp[rt][ct]))


if __name__ == '__main__':
    H, W = LI()
    # 1-index to 0-index
    rs, cs = list(map(lambda x:int(x)-1, input().split()))
    rt, ct = list(map(lambda x:int(x)-1, input().split()))
    main(H, W, rs, cs, rt, ct, [input() for h in range(H)])
