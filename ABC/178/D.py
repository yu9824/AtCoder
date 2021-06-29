# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)

'''
DP
A[n] = A[n-3] + A[n-4] + ... + A[0] (O(S**2))
ここで，A[n-1] = A[n-4] + A[n-5] + ... + A[0]より，
A[n] = A[n-3] + A[n-1]とも表せる．(O(S)でより高速．)
'''

mod = 10 ** 9 + 7
def main(*args):
    S = args[0]

    A = [0 for s in range(S+1)]
    A[0] = 1    # 何も足さない (= S自身のみの1通りを表すためのやつ．)
    
    s = 3
    while s <= S:
        # A[s] = sum(A[:(s-3)+1]) % mod # どっちでもOK．速いのは下のやつ．
        A[s] = (A[s-3] + A[s-1]) % mod
        s += 1
    print(A[S])


if __name__ == '__main__':
    args = [int(input())]
    main(*args)
    