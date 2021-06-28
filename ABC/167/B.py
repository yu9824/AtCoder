# list(map(int, input().split()))
# int(input())


def main(A, B, C, K):
    if K - A <= 0:
        print(K)
    elif K - A > 0 and K - A - B <= 0:
        print(A)
    else:
        print(A - (K - A - B))

if __name__ == '__main__':
    A, B, C, K = list(map(int, input().split()))
    main(A, B, C, K)
