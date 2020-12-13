# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)

from copy import copy
from math import ceil


def main(*args):
    N, M, A = args

    if M == 0:  # なかったら
        print(1)
    else:   # 青が一個でも
        # Aのそれぞれの間(A_bet)のリストを求めるための下準備．(python式index)
        copy_A = copy(sorted(A))
        copy_A.insert(0, -1)
        copy_A.append(N)

        # Aのそれぞれの間(A_bet)のリストを求める
        A_bet = [copy_A[i] - copy_A[i-1] - 1 for i in range(1, M+2) if copy_A[i] - copy_A[i-1] - 1 > 0] # それらを含まない '間' なので -1 をする．
        # print(A_bet)  # デバッグ用

        # 幅のうち0以外で一番小さな値を選択する場合が一番賢い．
        if len(A_bet) == 0: # 一個も白の場所がない場合
            print(0)
        else:
            k = min(A_bet)
            cnt = 0
            for diff in A_bet:
                cnt += ceil(diff / k)
            print(cnt)
    

if __name__ == '__main__':
    args = list(map(int, input().split()))
    args.append(list(map(lambda x:int(x)-1, input().split())))  # python式のindexに直す．
    main(*args)