# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)


# def main(N, K, A):
#     N, K, A
#
# if __name__ == '__main__':
#     N, K = list(map(int, input().split()))
#     A = [int(input()) for n in range(N)]
#     main(N, K, A)


mod = 998244353

def main(N, Q, LRD):
    s = '1' * N
    print(s)
    # for l, r, d in LRD:


if __name__ == '__main__':
    N, Q = list(map(int, input().split()))
    LRD = [tuple(map(int, input().split())) for q in range(Q)]
    main(N, Q, LRD)
