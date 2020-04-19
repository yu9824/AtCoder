def main(N, K):
    def sumN(x):
        return int(x * (x + 1) * 0.5)
    ans = sum([sumN(N) - sumN(N - k) - sumN(k - 1) + 1 for k in range(K, N + 2)])
    print(ans%(10**9+7))



if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    main(N, K)
