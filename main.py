# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)

def main(*args):
    a, b, x, y = args
    if a <= b:
        ans = (b - a) * min(y, 2 * x) + x
    else:   # a > b
        ans = (a - b - 1) * min(y, 2 * x) + x

    print(ans)
    

if __name__ == '__main__':
    args = list(map(int, input().split()))
    main(*args)
    