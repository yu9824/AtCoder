def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと

これグラフで，ダイクストラで求められるのでは？（なんとなく）
ダイクストラでは無理そう．（始点が決まっていないから）

N≤10だし普通に全探索？BFS?
見落としてたけど実行制限 5 secだった．

PyPy: 2341 ms
Python: TLE

実装に20分くらいかかったけど解けた．
解説: https://twitter.com/e869120/status/1390074137192767489

permutationで全探索しようと思ったけどTLEっぽくてやめちゃった．計算量的に行けそうってのは理解していたけどなんか無理そうだった．
permutationで普通にやったら普通に早かった．
PyPy: 418 ms
Python: TLE
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_af

from itertools import permutations

def main(*args):
    N, A, M, XY = args

    NG = [set() for n in range(N)]
    for x, y in XY:
        NG[x-1].add(y-1)
        NG[y-1].add(x-1)
    
    INF = 2 ** 32
    ans = INF
    for p in permutations(range(N)):    # 誰がどの区間を走るか
        cost = A[p[0]][0]   # p[0]: 1区間目を走る人
        for i in range(1, N):
            if p[i-1] in NG[p[i]]:  # 喧嘩していたならば
                break
            else:
                cost += A[p[i]][i]
        else:   # 最後までつながったら
            ans = min(ans, cost)
    print(ans if ans != INF else -1)

if __name__ == '__main__':
    N = int(input())
    A = [LI() for n in range(N)]
    M = int(input())
    main(N, A, M, [LI() for m in range(M)])
