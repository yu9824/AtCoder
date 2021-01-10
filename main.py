def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)


def main(*args):
    N, A, B = args

    x = 0
    for a, b in zip(A, B):
        x += a * b
    if x:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    args = [int(input())]
    for _ in range(2):
        args.append(LI())
    main(*args)