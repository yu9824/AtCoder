# list(map(int, input().split()))
# int(input())
from math import ceil

def main():
    N, X, T = list(map(int, input().split()))
    print(ceil(N / X) * T)

if __name__ == '__main__':
    main()
