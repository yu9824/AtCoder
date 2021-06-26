def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
# 思ったこと
n回操作すると
水色: LB = A + n * B
赤色: R = n * C

なりたいもの
D * R >= LB
D * n * C >= A + n * B
n * (C * D - B) >= A
'''

from math import ceil
def main(*args):
    A, B, C, D = args
    if C * D - B <= 0:
        print(-1)
    else:
        print(ceil(A / (C * D - B)))

if __name__ == '__main__':
    args = LI()
    main(*args)

