def main(N, K, d, A):
    a = list(set(sum(A, [])))
    print(N - len(a))

if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    d = []
    A = []
    for i in range(K):
        d.append(int(input()))
        A.append(list(map(int, input().split())))
    main(N, K, d, A)
