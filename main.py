def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)


def main(*args):
    N, A = args

    half = 2 ** (N-1)

    kessho = max(A[:half]), max(A[half:])
    print(A.index(min(kessho)) + 1)

    
    

if __name__ == '__main__':
    args = [int(input())]
    args.append(LI())
    main(*args)