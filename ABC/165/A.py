def main(K, A, B):
    a = int(A / K)
    b = int(B / K)
    if A == 0 or (a == b and A % K != 0):
        print('NG')
    else:
        print('OK')


if __name__ == '__main__':
    K = int(input())
    A, B = list(map(int, input().split()))
    main(K, A, B)
