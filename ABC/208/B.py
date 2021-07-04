def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと

'''

# https://atcoder.jp/contests/abc208/tasks/abc208_b

from math import factorial
def main(*args):
    P, = args
    kouka = []
    for n in range(10):
        kaijou = factorial(n+1)
        if kaijou > P:
            break
        kouka.append(kaijou)
    p = P
    ans = 0
    for kaijou in kouka[::-1]:
        shou = p // kaijou
        amari = p % kaijou
        if shou <= 100:
            ans += shou
            p = amari
        else:
            shou = 100
            ans += shou
            p -= kaijou * shou
        if p == 0:
            break
    print(ans)
        

if __name__ == '__main__':
    main(int(input()))
