def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと
普通にできそう．

Python: 179 ms
PyPy: 220 ms

解説: https://twitter.com/e869120/status/1376095755404861440
Pythonには set の中を in で高速に検索できるから解けた感じするけど言われてみればO(N^2)かかりそうな気がするのか，と思った．
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_aa

def main(*args):
    N, S = args
    st = set()
    for i, s in enumerate(S):
        if s not in st:
            print(i+1)
            st.add(s)


if __name__ == '__main__':
    N = int(input())
    main(N, [input() for n in range(N)])
