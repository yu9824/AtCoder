def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
思ったこと

すぐ解法がわかったので提出したが，WAで，それがなぜなのかわからず，解説を確認．
解説: https://twitter.com/e869120/status/1390436977808351234

「コーナーケースに気をつけよう」の通りだった．
最近本当にできなくて悲しくなってきちゃった．

1列もしくは1行のときは絶対条件を満たすことはないので全部をつけてOKって話だった．

Python: 27 ms
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_ag

def main(*args):
    H, W = args
    
    ans = max(H, W) if H == 1 or W == 1 else ((H + 1) // 2) * ((W + 1) // 2)
    print(ans)

if __name__ == '__main__':
    main(*LI())
