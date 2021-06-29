# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)


# 解説通り
# 読んでも何言ってるか何もわからん．
def main(*args):
    N, M, A, B = args

    dp = [[-1 for m in range(M+1)] for n in range(N+1)]

    for n in range(N+1):
        for m in range(M+1):
            if n == 0:
                dp[n][m] = m
            elif m == 0:
                dp[n][m] = n
            else:
                '''
                A[n-1]を消すとき (xが1増える)
                B[m-1]を消すとき (xが1増える)
                どちらも消さず，A_prime[-1] = A[n-1], B_prime[-1] = B[m-1]になるようにするしかない．(yはA[n-1]とB[m-1]が一致しているかどうかに依存して増加しうる．xは増加し得ない．)
                '''
                dp[n][m] = min(dp[n-1][m] + 1, dp[n][m-1] + 1, dp[n-1][m-1] + (A[n-1] != B[m-1]))
    print(dp[-1][-1])

    

if __name__ == '__main__':
    args = list(map(int, input().split()))
    args.append(list(map(int, input().split())))
    args.append(list(map(int, input().split())))
    main(*args)