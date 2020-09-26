# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)

# def main(A, B, C, D):
#     if A <= C <= B or C <= B <= D:
#         print('Yes')
#     else:
#         print('No')
#
# if __name__ == '__main__':
#     A, B, C, D = list(map(int, input().split()))
#     main(A, B, C, D)

def main():
    K = int(input())
    s = ''
    for k in range(K):
        s += 'ACL'
    print(s)

if __name__ == '__main__':
    main()
