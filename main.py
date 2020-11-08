# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)

def main(*args):
    N, A = args

    ans = 0
    maximum = 0
    for i in range(2, max(A)+1):
        cnt = 0
        for a in A:
            if a % i == 0:
                cnt += 1
        else:
            if cnt > maximum:
                maximum = cnt
                ans = i
    print(ans)
    

if __name__ == '__main__':
    args = [int(input())]
    args.append(list(map(int, input().split())))
    main(*args)
