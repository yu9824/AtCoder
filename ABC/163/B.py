def main(N, M, A):
    memo = N - sum(A)
    if memo >= 0:
        return memo
    else:
        return -1

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    # N = 314
    # M = 15
    # A = list(map(int, "9 26 5 35 8 9 79 3 23 8 46 2 6 43 3".split()))
    # print(N, M, A)
    print(main(N, M, A))
