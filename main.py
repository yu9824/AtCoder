def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

def main(*args):
    C = set(list(input()))
    if len(C) == 1:
        print('Won')
    else:
        print('Lost')
    

if __name__ == '__main__':
    args = []
    main(*args)