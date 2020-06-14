# list(map(int, input().split()))
# int(input())


def main(X, N, P):
    st = set(P)
    if N == 0:
        print(X)
    else:
        n = 0
        while True:
            if X - n not in st:
                print(X - n)
                exit()
            elif X + n not in st:
                print(X + n)
                exit()
            else:
                n += 1

if __name__ == '__main__':
    X, N = list(map(int, input().split()))
    P = list(map(int, input().split()))
    main(X, N, P)
