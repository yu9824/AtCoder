import math

def main(A, B, C, D):
    TAKAHASHI = math.ceil(C / B)
    AOKI = math.ceil(A / D)
    # print(TAKAHASHI, AOKI)
    if TAKAHASHI <= AOKI:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    A, B, C, D = list(map(int, input().split()))
    main(A, B, C, D)
