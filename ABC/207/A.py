def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
# 思ったこと
'''

MOD = 10**9+7
def main(*args):
    args, = args
    args.sort()
    print(args[-1] + args[-2])
   

if __name__ == '__main__':
    args = LI()
    main(args)

