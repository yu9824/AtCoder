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
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_aq

from collections import deque

def main(*args):
    H, W, rs, cs, rt, ct, S = args
    dp = [[INF] * W for h in range(H)]

    OK = '.'
    NG = '#'
    lst_direction = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def get_candidate(x, y):
        for direction, (k, l) in enumerate(lst_direction):
            y_cand = y+k
            x_cand = x+l
            if 0 <= y_cand < H and 0 <= x_cand < W:
                yield ((x_cand, y_cand), direction)

    dp[rs][cs] = 0
    # [(i, j), direction_pre]
    # direction_pre: lst_directionに示されたもののうちどの方角か．どれでもないときは-1．(i-1,j-1)から(i,j)にいくとき．
    que = deque([[(cs, rs), -1]])
    while que:
        # print(que)
        (x, y), direction_pre = que.popleft()
        for (x_cand, y_cand), direction in get_candidate(x, y):
            if S[y_cand][x_cand] == OK: # 道ならば
                if direction_pre == -1 or direction_pre == direction:   # 直進してきた場合
                    cost = dp[y][x]
                else:   # 曲がる必要がある場合
                    cost = dp[y][x] + 1
                cost_cand = dp[y_cand][x_cand]
                if cost_cand >= cost:   # 更新できるならば
                    dp[y_cand][x_cand] = cost
                    que.append([(x_cand, y_cand), direction])
    print(dp[rt][ct])


if __name__ == '__main__':
    H, W = LI()
    # 1-index to 0-index
    rs, cs = list(map(lambda x:int(x)-1, input().split()))
    rt, ct = list(map(lambda x:int(x)-1, input().split()))
    main(H, W, rs, cs, rt, ct, [input() for h in range(H)])
