def main(N, D, T):
    for i in range(N - 1):
        if T[i + 1] - T[i] <= D:
            print(T[i+1])
            break
    else:
        print(-1)


if __name__ == "__main__":
    N, D = map(int, input().split())
    T = list(map(int, input().split()))
    main(N, D, T)
