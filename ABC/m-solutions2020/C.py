# list(map(int, input().split()))
# int(input())

def main(N, K, A):
    for i in range(K, N): # 0 から数えるから K-1
        this = A[i]
        before = A[i-K]

        if this > before:
            print('Yes')
        else:
            print('No')



if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    main(N, K, A)
