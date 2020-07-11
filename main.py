# list(map(int, input().split()))
# int(input())

from collections import Counter

def main(N, X):
    lst = list(X)
    num = lst.count('1')
    print(num)
    # for n in range(N):


if __name__ == '__main__':
    N = int(input())
    X = int(input())
    main(N, X)
