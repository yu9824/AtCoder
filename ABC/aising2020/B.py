# list(map(int, input().split()))
# int(input())

def main(N, A):
    ans = 0
    for n in range(1, N+1, 2):
        if A[n-1] % 2 == 1:
            ans += 1
    print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    main(N, A)
