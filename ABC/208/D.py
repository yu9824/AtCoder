def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと
有向グラフってやつでしょうか？
隣接行列？
N ≤ 400だから普通に全探索やればいける？
'''

def main(*args):
    N, M, ABC = args
    graph = [[-1 for n in range(N)] for nn in range(N)]

    # graph[a][b]: a to b
    for a, b, c in ABC:
        graph[a][b] = c
    print(graph)


if __name__ == '__main__':
    N, M = LI()
    main(N, M, [list(map(lambda x:int(x)-1, input().split())) for m in range(M)])
