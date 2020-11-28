# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)

from math import sqrt, ceil

def main(*args):
    n = args[0]

    # 長さn + 1の丸太を買うことで何本 (i本) 節約できるかを計算．
    s = lambda x: x * (x + 1) // 2  # 総和求める関数
    
    # iを全部やってるとめっちゃ時間かかるのであたりをつける．
    i = ceil(sqrt(2 * (n + 1)))
    while s(i) >= n + 1:
        i -= 1
    
    # n+1の長さの丸太から，小さいほうからi本のマルタを作ることができる（捨ててOKなので)
    ans = n - i + 1
    print(ans)
    

if __name__ == '__main__':
    args = [int(input())]
    main(*args)
    