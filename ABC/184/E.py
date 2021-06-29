# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)


# 幅優先探索
# pythonだとTLE, pypyで通った．
from collections import deque

# 定数
code_a = ord('a')

def main(*args):
    H, W, A, S, G, tele = args
    # print(H, W, A, S, G, tele)

    # 移動候補
    d = ((0, 1), (1, 0), (0, -1), (-1, 0))


    cost = [[float('inf') for w in range(W)] for h in range(H)]
    cost[S[0]][S[1]] = 0
    # print(cost)

    que = deque([S])
    while que:
        x, y = que.popleft()
        nextcost = cost[x][y] + 1
        for dx, dy in d:
            x2 = x + dx
            y2 = y + dy
            if x2 < 0 or x2 >= H or y2 < 0 or y2 >= W or A[x2][y2] == '#':  # 範囲外 or 移動できない場所だった場合．
                continue
            if cost[x2][y2] > nextcost: # まだ訪れていない or これより高コストで来ることになっている場合
                cost[x2][y2] = nextcost
                que.append((x2, y2))    # 移動先候補として追加
        if A[x][y].islower():   # テレポートできるなら
            i = ord(A[x][y]) - code_a
            for x2, y2 in tele[i]:
                if cost[x2][y2] > nextcost: # まだ訪れていない or これより高コストで来ることになっている場合
                    cost[x2][y2] = nextcost
                    que.append((x2, y2))    # 移動先候補として追加
            tele[i].clear() # 一回使ったテレポーターは戻るのに使われるだけで最短ルートには不要なのでクリア．
    ans = cost[G[0]][G[1]]
    if ans == float('inf'):
        ans = -1
    print(ans)
    

if __name__ == '__main__':
    H, W = list(map(int, input().split()))
    args = [H, W]
    A = []
    tele = [[] for i in range(26)]
    for h in range(H):
        a = input()
        for w in range(W):
            if a[w] == 'S':
                S = [h, w]
            elif a[w] == 'G':
                G = [h, w]
            elif a[w].islower():
                tele[ord(a[w])-code_a].append((h, w))
        A.append(a)
    args.extend([A, S, G, tele])
    main(*args)
    