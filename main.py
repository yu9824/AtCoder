# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)


def main(*args):
    N, X, S = args
    
    ans = X
    n = 0
    while n < N:
        if S[n] == 'o':
            ans += 1
        else:
            ans = max(0, ans - 1)
        n += 1
    print(ans)

if __name__ == '__main__':
    args = list(map(int, input().split())) + [input()]
    main(*args)
    