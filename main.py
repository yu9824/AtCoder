from collections import deque

# numpy使ったらめっちゃおそくなった (np.whereなのか，リストをnumpyに変換するのがダメなのか，numpyの座標指定からの値returnが遅いのか不明だが．少なくとも半分未満にはなっている．)

def main(H, W, c):
    for i in range(H):
        for j in range(W):
            if c[i][j] == 's':
                start = [i, j]
            elif c[i][j] == 'g':
                goal = [i, j]

    want = deque([start])    # 次の探索候補地をためておくque
                            #スタート地点を候補地として代入
    cost = [[-1] * W for _ in range(H)]   # 何回壊したらそこまで最短でいけるのかを示した配列．まだいけてない場合は-1で調査したかしてないかの区別もつけている．
    cost[start[0]][start[1]] = 0    # スタート地点は壊さなくても到達できるので0を代入 (初期条件)

    candidate = [[1, 0], [0, 1], [-1, 0], [0, -1]]   # ある座標から動ける候補の動き方

    while len(want):    # 調査してない候補地がある限り
        now = want.popleft()    # FIFOで候補地を探索するとして，
        for cand in candidate:  #すべての移動候補地について
            next = [now[0] + cand[0], now[1] + cand[1]]
            if OK(*next) and cost[next[0]][next[1]] == -1:  # 未探索+街の中なら
                if c[next[0]][next[1]] == '#':    #壁を壊す場合：探索優先順位が低い→queの右から足す
                    cost[next[0]][next[1]] = cost[now[0]][now[1]] + 1
                    want.append(next)
                else:   #壁を壊さない場合：探索優先順位が高い→queの左から足して次に探索させる．
                    cost[next[0]][next[1]] = cost[now[0]][now[1]]
                    want.appendleft(next)
                if next == goal:
                    if cost[goal[0]][goal[1]] <= 2:
                        print('YES')
                    else:
                        print('NO')
                    exit()
                elif cost[now[0]][now[1]] > 2:
                    print('NO')
                    exit()
    # print(c, cost)


def OK(h, w):
    return 0 <= h and h < H and 0 <= w and w < W


if __name__ == '__main__':
    H, W = list(map(int, input().split()))
    c = [list(input()) for i in range(H)]
    main(H, W, c)
