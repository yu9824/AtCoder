# list(map(int, input().split()))
# int(input())

def main(K):
    lst = [i for i in range(1, 10)]
    K_str = str(K)
    if K_str[-1] in ['0', '2', '4', '5', '6', '8']:
        print(-1)
    else:
        counta = 1
        a = 7
        amari_memo = 70 % K
        while a % K:
            counta += 1
            a = a % K + amari_memo
            amari_memo = amari_memo * 10 % K
        print(counta)


if __name__ == '__main__':
    K = int(input())
    main(K)
