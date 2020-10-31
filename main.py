# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)

mod = 998244353

def main(*args):
    A, B, C = args
    sumA = (A * (A + 1)) // 2
    sumB = (B * (B + 1)) // 2
    sumC = (C * (C + 1)) // 2
    print((sumA * sumB * sumC) % mod) 

if __name__ == '__main__':
    args = list(map(int, input().split()))
    main(*args)



    