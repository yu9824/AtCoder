# list(map(int, input().split()))
# int(input())
from itertools import combinations_with_replacement

def main(lst, K):
    # 要するにC>B>Aになればおけ．
    c = combinations_with_replacement([0, 1, 2], K)
    print(c)

if __name__ == '__main__':
    lst = list(map(int, input().split()))
    K = int(input())
    main(lst, K)
