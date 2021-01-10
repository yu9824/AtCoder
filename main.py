def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)


def main(*args):
    A = min(args)
    B = max(args)
    if A + 3 > B:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    args = LI()
    main(*args)