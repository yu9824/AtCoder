def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと
累積和みたいにやればいけるのでは？
配列のそれまでに出てきた種類と数を保存する．

連続する部分をひとまとまりにする？

REやTLEにはまったので解説を見た．
解説: https://twitter.com/e869120/status/1390798852299448322

考え方は合っていた．ただ自分のやろうとしている実装が複雑すぎるのでおかしいなとは思った．
尺取り法というらしい．

絶対増えること（単調増加）を生かして問題を解くらしい．

参考コード: https://github.com/hibit-at/typical90/blob/main/34.py

$O(n^2)$ → $O(n \mathrm{log}\ n)$
- [034.py](./034.py)

- キーワード
  - 広義単調増加関数．

参考: [しゃくとり法 (尺取り法) の解説と、それを用いる問題のまとめ - Qiita](https://qiita.com/drken/items/ecd1a472d3a0e7db8dce)


結局参考コードのやり方をまるパクリ（自分で書いたけど）することになった．
長さを求める部分を何回もやると重いっぽい．だからあえて，それを外の整数の変数で持っておくことで高速化できた．

この考え方はよく使いそう．

Python: 110 ms
PyPy: 116 ms
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_ah

from collections import deque
def main(*args):
    N, K, A = args
    
    lx = 0
    la = A[lx]
    que = deque([la])
    len_que = 1
    ans = 0
    d_num = {
        la:1
    }   # 何が何個入っているか
    kinds = 1   # 何種類の数字？

    rx = 1
    while rx < N:
        ra = A[rx]

        if ra in d_num:
            d_num[ra] += 1
        else:
            kinds += 1
            d_num[ra] = 1
        
        que.append(ra)
        len_que += 1
        
        # TLEはおそらくlen(set(que))のせいな気がする．→数の種類に関する変数を別にを持っておこう．
        # while len(set(que)) > K:
        while kinds > K:
            la = que.popleft()
            len_que -= 1
            if d_num[la] == 1:  # 最後の一個ならば
                kinds -= 1
                d_num.pop(la)
            else:
                d_num[la] -= 1
        ans = max(ans, len_que)
        rx += 1
    print(ans)

if __name__ == '__main__':
    N, K = LI()
    main(N, K, LI())
