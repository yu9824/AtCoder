def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと

UnionFindではできないな．
木の取り扱いは隣接行列と隣接リストしか知らないけど，とりあえずそれでやってみよう．

木の直径が2以上な組み合わせを探せばいいのでは？

全くわからないので解説を見る．
解説: https://twitter.com/e869120/status/1387175538544975872

「二部グラフの性質を使おう」そもそも二部グラフを知らない．
二部グラフ
- 奇数長の閉路を含まない．
- 最大マッチングが多項式時間で計算できる．←さっぱりわからない．

木は必ず二部グラフなので，という考え方らしい．
そもそも問題文を二色の彩色問題に読み替えることが自分にはできないので解説をすぐみて正解．

正直そもそも解けるようになる気もあまりしない．

計算量O(N)で解けるらしい．
DFSは一回リフレッシュしたら書けた．
0-indexにしたのを1-indexにするのを忘れるなど，細かい実装ミスが発生した．

再帰関数の方をやってみても練習になるかも．

Python: 373ms
PyPy: 284ms
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_z

def main(*args):
    N, AB = args
    # 隣接リスト
    graph = [[] for n in range(N)]
    for a, b in AB:
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

    # 0, 1の二色で塗り分け．
    groups = [[], []] # color0のグループとcolor1のグループ
    already = [False for n in range(N)] # 色をすでに塗ったか否か
    from collections import deque
    cand = deque([(0, 0)])  # (position, color)
    while cand:
        # 今着目してるノード
        position, color = cand.pop()
        already[position] = True

        # 次に見て欲しいノード
        for next_position in graph[position]:
            if not already[next_position]:
                cand.append((next_position, color^1))    # ^1で0を1に，1を0にできる．

        groups[color].append(position)
    
    get_ans = lambda y:' '.join(list(map(lambda x:str(x+1), y))[0:N//2])
    ans = get_ans(groups[0]) if len(groups[0]) >= N//2 else get_ans(groups[1])
    print(ans)

if __name__ == '__main__':
    N = int(input())
    main(N, {tuple(LI()) for n in range(N-1)})
