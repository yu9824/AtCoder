# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)


def main(*args):
    print(max(int(input()), 0))

if __name__ == '__main__':
    main()
