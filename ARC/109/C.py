# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)

def winner(s):
    if len(s) == 2:
        st = set(list(s)) if type(s) == str else set(s)
        if len(st) == 1:    # あいこ
            return s[0]
        elif 'R' in st and 'P' in st:
            return 'P'
        elif 'P' in st and 'S' in st:
            return 'S'
        else:
            return 'R'
    else:
        raise ValueError('"' + str(s) + '"が入力されました．')

def main(*args):
    n, k, s = args

    # 解説通り脳死
    s = list(s)
    for i in range(k):
        s *= 2
        for j in range(n):
            s[j] = winner(s[2*j:2*(j+1)])
        s = s[:n]
    print(s[0])
    

if __name__ == '__main__':
    args = list(map(int, input().split())) + [input()]
    main(*args)