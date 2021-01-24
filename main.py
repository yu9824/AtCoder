def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

from collections import Counter

def main(*args):
    N, K, A = args

    c = Counter(A)
    max_A = max(c)

    def reculsive(i = 0, k = K):
        '''
        iを入れられない箱を取り除いていく．

        i: 着目しているボールの数（小さい方から順番に行く）
        k: まだ除かれず，残っている箱の数
        '''
        
        # x: iが書かれたボールの個数
        x = c[i] if i in c else 0

        # 何個の箱がここで削除されたか．
        if k > x:   # 箱が削除されるならば
            # 削除された箱の数を求める．
            diff = k - x
            # kの更新
            k = x
        else:
            diff = 0

        if i == max_A:    # 最大値をとってもなお箱が残っていたら
            return diff * i + k * (i+1)
        else:
            # ここで消えた箱の分だけ足す．→ここで消えた = i-1の数までのボールが入ってる = 箱にはiが表示されるものがdiff個存在
            return diff * i + reculsive(i+1, k)

    print(reculsive())

    

if __name__ == '__main__':
    args = LI()
    args.append(LI())

    main(*args)