def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと

を，超える場合は，なので<=だった．
Python: 33 ms

Pythonだと簡単だけどほかだと難しいのかもしれない．

問題点はgcdの実装ではなく，オーバーフローだった．
Pythonだとあまり考えなくてもいいが，2**63-1を途中で超えてしまうとダメ，って話らしい．
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_al


from math import gcd
def lcm(a, b): return a * b // gcd(a, b)

def main(*args):
    ans = lcm(*args)
    ans = ans if ans <= 10 ** 18 else 'Large'
    print(ans)


if __name__ == '__main__':
    main(*LI())
