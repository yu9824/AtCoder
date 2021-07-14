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
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_aq

from collections import deque

def main(*args):
    H, W, rs, cs, rt, ct, S = args
    dp = [[INF] * W for h in range(H)]
    visited = [[False]*W for h in range(H)]

    OK = '.'
    NG = '#'
    lst_direction = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def get_candidate(x, y, direction_pre = -1):
        for direction, (k, l) in enumerate(lst_direction):
            y_next = y+k
            x_next = x+l
            if 0 <= y_next < H and 0 <= x_next < W:
                yield ((y_next, x_next), direction, direction_pre)

    dp[rs][cs] = 0
    visited[rs][cs] = True
    # [(i, j), direction, direction_pre]
    # direction: lst_directionに示されたもののうちどの方角か．どれでもないときは-1．(i-1,j-1)から(i,j)にいくとき．
    # straight: 前回からの方角．(i-2,j-2)から(i-1,j-1)にいくとき
    que = deque([[(rs, cs), -1, -1]])
    while que:
        (y, x), direction, direction_pre = que.popleft()
        if S[y][x] == OK:   # 道ならば
            y_pre = y - lst_direction[direction][0]
            x_pre = x - lst_direction[direction][1]
            if direction_pre == -1 or direction == direction_pre: # 直進してきた場合
                cost = dp[y][x]
                cost_cand = dp[y_pre][x_pre]    # そのままの値を代入
                if cost > cost_cand:    # 更新できるならば
                    dp[y][x] = cost_cand
                else:
                    continue    # 次の候補を追加せず戻る
            else:   # 曲がることになった場合
                cost = dp[y][x]
                cost_cand = dp[y_pre][x_pre] + 1    # 曲がった回数を追加
                if cost > cost_cand:    # 更新できるならば
                    dp[y][x] = cost_cand    # 更新
                else:
                    continue    # 次の候補を追加せず戻る
            # 次の候補を追加
            for args in get_candidate(x, y, direction_pre=direction):
                que.append(args)
                print(que)

    print(dp[rt][ct])
    





if __name__ == '__main__':
    H, W = LI()
    # 1-index to 0-index
    rs, cs = list(map(lambda x:int(x)-1, input().split()))
    rt, ct = list(map(lambda x:int(x)-1, input().split()))
    main(H, W, rs, cs, rt, ct, [input() for h in range(H)])
