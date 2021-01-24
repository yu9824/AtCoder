def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

from collections import Counter

def main(*args):
    N, K, A = args

    c = Counter(A)
    max_A = max(c)  # 辞書のmaxはkeyの最大値を返すのでこれでOK

    # 捨てずに残っている箱の数
    k = K
    
    cnt = 0
    # 最大値+1までやれば最大値をとってもなお消えない箱を消してすべての箱の値を足し算することが可能．
    for i in range(max_A+2):
        if k > c[i]:
            # iが書かれたボールの数
            x = c[i]

            # 何個箱を捨てるか
            diff = k - x
            cnt += diff * i

            # kの更新
            k = x
    print(cnt)

    

if __name__ == '__main__':
    args = LI()
    args.append(LI())

    main(*args)