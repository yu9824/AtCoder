def main(N, M, H, AB):
    bad = []
    for A, B in AB:
        if H[A - 1] >= H[B - 1]: #pythonは一個ずれる
            bad.append(B)
        if H[B - 1] >= H[A - 1]:
            bad.append(A)
    print(N - len(list(set(bad))))

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    H = list(map(int, input().split()))
    AB = []
    for i in range(M):
        AB.append(list(map(int, input().split())))
    main(N, M, H, AB)
