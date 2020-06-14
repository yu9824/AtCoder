# list(map(int, input().split()))
# int(input())


def main(X, Y):
    cand = Y // 4
    for i in range(cand, -1, -1):
        if i * 4 + (X - i) * 2 == Y:
            print('Yes')
            exit()
    else:
        print('No')
if __name__ == '__main__':
    X, Y = list(map(int, input().split()))
    main(X, Y)
