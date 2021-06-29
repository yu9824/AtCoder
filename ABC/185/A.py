# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)


def main(*args):
    print(min(args))
    

if __name__ == '__main__':
    args = list(map(int, input().split()))
    main(*args)