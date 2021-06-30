def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
# 思ったこと
ガチで円運動では？
y = -(L/2) * sin(omega * t)
z = (L/2) * (1 - cos(omega * t))

なんか通った．
誤差に言及されていたのでDecimal必要かと思ったけどそんなことはなかった．

Python: 30 ms
PyPy: 85 ms

解説: https://twitter.com/e869120/status/1384276005330690049/
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_r

from math import sin, cos, pi, asin, sqrt
def main(*args):
    T, L, X, Y, Q, E = args
    omega = 2 * pi / T
    get_y = lambda t:-(L/2) * sin(omega * t)
    get_z = lambda t:(L/2) * (1 - cos(omega * t))
    for e in E:
        y1 = get_y(e)
        z1 = get_z(e)
        print(asin(z1 / sqrt(X ** 2 + (Y - y1) ** 2 + z1 ** 2))/pi*180)

if __name__ == '__main__':
    T = int(input())
    L, X, Y = LI()
    Q = int(input())
    E = [int(input()) for q in range(Q)]
    main(T, L, X, Y, Q, E)

