def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと

'''

# https://atcoder.jp/contests/abc208/tasks/abc208_a

def main(*args):
    a, b = args
    if 6 * a >= b >= a:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main(*LI())
