def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
# 思ったこと
化学式でこれの判定をやったことがあるので行けそう
1から増やしていけばできそう．それらの二つの組み合わせ的な．

区切りを入れる場所を総当たりすれば行けそう．

実装できないので答えを見る．
#Nが小さい→全探索
#'('と')'の二つ→bit全探索

考え方としては全探索で適当に作って，それが正しいかっこの条件を満たしているかを確認する必要がある．
********* 正しいカッコの条件 *********
- これまででてきた閉じカッコの数が開きカッコのかずより同じかそれより小さい
- 最終的に閉じカッコと開きカッコの数が同じ．
************************************

解答: https://twitter.com/e869120/status/1377391097836544001
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_b



def main(*args):
    N, = args
    l = '('
    r = ')'

    answers = []
    for b in range(2 ** N):
        s = ''
        cnt_zero = 0    # 閉じカッコの数
        cnt_one = 0     # 開きカッコの数
        for i in range(N):
            if b >> i & 1:
                s += l
                cnt_one += 1
            else:
                s += r
                cnt_zero += 1
            if cnt_one < cnt_zero:  # 閉じカッコのかずのほうが多くなってしまった場合は絶対ダメなので
                break
        if cnt_one == cnt_zero:
            answers.append(s)
    
    {print(s) for s in sorted(answers)}

                

    # answers = set()
    # if N % 2 == 0:
    #     n_pair = N // 2
    #     for i in range(n_pair+1):
    #         lst = []
    #         for x in range(i):
    #             [lst.append(x) for _ in range(x+1)]
    #         c = combinations(lst, i)
    #         for j in c:
    #             temp = list(l * n_pair)
    #             for k in sorted(j):
    #                 temp[k] += r
    #             temp.append(r*(n_pair-i))
    #             s = ''.join(temp)
    #             answers.add(s)
    # {print(s) for s in sorted(list(answers))}
    # print(len(answers))
    
    


if __name__ == '__main__':
    N = int(input())
    main(N)

