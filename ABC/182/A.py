# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)


def main(*args):
    A, B = args
    print(2 * A + 100 - B)
    

if __name__ == '__main__':
    args = list(map(int, input().split()))
    main(*args)
