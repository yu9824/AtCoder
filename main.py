def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
# 思ったこと
事前に縦と横の合計しらべればいいのでは？そのあと取り出すイメージ．
O(HW)でもギリいける?
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_d

import numpy as np
from numba import jit

def main(*args):
    H, W, A = args
    A = np.array(A, dtype=int)

    answers = get_answers(A)
    for h in range(H):
        print(' '.join(answers[h].astype(str)))

    # A = sumH + sumW - A

    # sum_W = []
    # sum_H = []
    # for w in range(W):
    #     print(A[:, w])
    #     sum_W.append(sum(A[:][w]))
    # for h in range(H):
    #     sum_H.append(sum(A[h]))
    # print(sum_W, sum_H)
    
    # for h in range(H):
    #     print(' '.join([str(sum_W[w] + sum_H[h] - A[h][w]) for w in range(W)]))

@jit('i8[:,:](i8[:,:])')
def get_answers(A):
    sumH = A.sum(axis=1).reshape(-1, 1)
    sumW = A.sum(axis=0)
    return sumH + sumW - A
    

if __name__ == '__main__':
    H, W = LI()
    A = [LI() for h in range(H)]
    main(H, W, A)

