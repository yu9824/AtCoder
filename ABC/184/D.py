# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)


# メモ再帰DP
# きちんとした立式ができるかどうかな気がする．

# 定数
code_a = ord('a')

def main(*args):
    A, B, C = args

    def cal(X, Y, Z, memo = {}):
        S = X + Y + Z
        key = (X, Y, Z)
        if 100 in key:
            return 0
        elif key in memo:
            return memo[key]
        else:
            X2 = X / S * (cal(X+1, Y, Z, memo) + 1) if X else 0
            Y2 = Y / S * (cal(X, Y+1, Z, memo) + 1) if Y else 0
            Z2 = Z / S * (cal(X, Y, Z+1, memo) + 1) if Z else 0
            value = X2 + Y2 + Z2
            memo[key] = value
            return value

    ans = cal(A, B, C)
    print('{:.7f}'.format(ans))
    

if __name__ == '__main__':
    args = list(map(int, input().split()))
    main(*args)
    