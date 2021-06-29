def LI(): return list(map(int, input().split()))
def I(): return int(input())

import sys
sys.setrecursionlimit(10 ** 9)


def main(*args):
    A, B = args
    S = lambda x: sum([int(n) for n in x])
    print(max(S(A), S(B)))

if __name__ == '__main__':
    args = input().split()
    main(*args)