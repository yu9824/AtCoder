# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)


def main(*args):
    a, b, c, d = args
    print(a * d - b * c)

if __name__ == '__main__':
    args = list(map(int, input().split())) + list(map(int, input().split()))
    main(*args)
    