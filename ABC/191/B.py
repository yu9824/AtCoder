def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)


def main(*args):
    N, X, A = args

    ans = [str(a) for a in A if a != X]
    print(' '.join(ans))
    

if __name__ == '__main__':
    args = LI()
    args.append(LI())
    main(*args)