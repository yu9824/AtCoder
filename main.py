def main(N, S):
    print(len(set(S)))


if __name__ == '__main__':
    S = []
    N = int(input())
    for i in range(N):
        S.append(input())
    main(N, S)
