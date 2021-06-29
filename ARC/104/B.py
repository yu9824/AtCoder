# list(map(int, input().split()))
# int(input())

from pdb import set_trace

from copy import copy
import sys
sys.setrecursionlimit(10 ** 9)

# 累積和?


def main(N, S):
    p1 = {'G', 'C'}
    p2 = {'A', 'T'}
    p = ['A', 'T', 'G', 'C']

    memo = [0, 0, 0, 0]
    ruiseki = [copy(memo)]
    ans = 0
    for i in range(N):
        memo[p.index(S[i])] += 1
        ruiseki.append(copy(memo))

    def subtract(lst1, lst2, i):
        return lst1[i] - lst2[i]

    for j in range(N+1-2):
        for k in range(j+2, N+1):
            lst1 = ruiseki[k]
            lst2 = ruiseki[j]
            if subtract(lst1, lst2, 0) == subtract(lst1, lst2, 1) and subtract(lst1, lst2, 2) == subtract(lst1, lst2, 3):
                ans += 1
    print(ans)



    # set_trace()



if __name__ == '__main__':
    # N = 5000
    # S = 'ATGC' * 1250
    # print(S)

    N, S = input().split()
    N = int(N)

    # N, S = 4, 'AGCT'


    main(int(N), S)
