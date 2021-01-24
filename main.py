def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

def main(*args):
    N, S = args

    # Trueとなる通り数．Xのindexで指定
    def reculsive(n):
        '''
        n: 何番目．1-index
        '''
        if n == 0:
            return 1
        oper = S[n-1]
        if oper == 'OR':
            '''
            x_nがTrue: 0 ~ (n-1)がTrue，FalseなんでもOK → 2 ** n
            x_nがFalse: Trueじゃなきゃいけないのでreculsive(n-1)
            '''
            return 2 ** n + reculsive(n-1)
        else:   # oper == 'AND'
            '''
            x_nがTrue: Trueじゃなきゃいけないのでreculsive(n-1)
            x_nがFalse: 絶対無理．0．
            '''
            return reculsive(n-1)

    print(reculsive(N))

    

if __name__ == '__main__':
    N = int(input())
    args = [N]
    args.append([input() for n in range(N)])

    main(*args)