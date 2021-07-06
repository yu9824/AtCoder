def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと
有向グラフってやつでしょうか？
隣接行列？
N ≤ 400だから普通に全探索やればいける？

経路問題の本質を理解していればできたらしい．
ついでに他の経路問題もlibrary.pyに足してみようかな．

3秒制約問題
PyPy: 1925 ms
Python: TLE
'''

def main(*args):
    N, M, ABC = args
    INF = 2 ** 32
    graph = [[INF if n != nn else 0 for n in range(N)] for nn in range(N)]

    # graph[a][b]: a to b
    for a, b, c in ABC:
        graph[a-1][b-1] = c

    ans = 0
    for k in range(N):
        for s in range(N):
            for t in range(N):
                new_cost = min(graph[s][t], graph[s][k] + graph[k][t])
                ans += new_cost % INF
                graph[s][t] = new_cost
    print(ans)



if __name__ == '__main__':
    N, M = LI()
    main(N, M, [LI() for m in range(M)])
