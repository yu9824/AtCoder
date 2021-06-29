# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)

def main(*args):
    N = args[0]
    if N % 2 == 0:
        print('White')
    else:
        print('Black')

    

if __name__ == '__main__':
    args = list(map(int, input().split()))
    main(*args)
    