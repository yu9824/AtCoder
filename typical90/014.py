def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
# 思ったこと
ソートしたら終わりでは？
→終わりだった．

PythonでもPyPyでも実行時間はほとんど変わらず．
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_n


def main(*args):
    N, A, B = args
    E = 0
    for a, b in zip(sorted(A), sorted(B)):
        E += abs(a-b)
    print(E)

if __name__ == '__main__':
    N = int(input())
    A = LI()
    B = LI()
    
    main(N, A, B)

