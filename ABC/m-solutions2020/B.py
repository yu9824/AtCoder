# list(map(int, input().split()))
# int(input())
from itertools import combinations_with_replacement
import copy

def main(lst, K):
    original = copy.copy(lst)
    # 要するにC>B>Aになればおけ．
    comb = combinations_with_replacement([0, 1, 2], K)
    for c in comb:
        lst = copy.copy(original)
        for i in c:
            lst[i] *= 2
            if lst[0] < lst[1] and lst[1] < lst[2]:
                print('Yes')
                exit()
    print('No')

if __name__ == '__main__':
    lst = list(map(int, input().split()))
    K = int(input())
    main(lst, K)
