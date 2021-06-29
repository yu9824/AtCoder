# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)

# いもす法
# https://imoz.jp/algorithms/imos_method.html
lim = 2 * 10 ** 5

def main(*args):
    N, W = args[:2]
    schedules = args[2:]

    # table = [0 for _ in range(lim)]   2 * 10 ** 5というindexをもつ箱も使いうるので range(2 * 10 ** 5 + 1)とする必要がある．
    table = [0 for _ in range(lim+1)]

    i = 0
    while i < N:
        s, t, p = schedules[i]
        # table[s-1] += p   # 時刻0から始まる可能性があるのでダメ．2 * 10 ** 5というindexをもつ箱も使いうるので range(2 * 10 ** 5 + 1)とする必要がある．
        # table[t-1] -= p
        table[s] += p
        table[t] -= p
        i += 1
    
    j = 0
    # while j < lim:
    #     if j > 0:
    #         table[j] += table[j-1]
    #     j += 1
    while j < lim:
        table[j+1] += table[j]
        j += 1
    
    if max(table) > W:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    N, W = list(map(int, input().split()))
    args = [N, W]
    for n in range(N):
        s, t, p = list(map(int, input().split()))
        args.append([s, t, p])
    main(*args)
