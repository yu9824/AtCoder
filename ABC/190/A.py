def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

from math import ceil

def main(*args):
    A, B, C = args
    if C:
        if B > A:
            ans = 'Aoki'
        else:
            ans = 'Takahashi'
    else:
        if A > B:
            ans = 'Takahashi'
        else:
            ans = 'Aoki'
    print(ans)

if __name__ == '__main__':
    args = LI()

    main(*args)