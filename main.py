# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)

from collections import Counter

def main(*args):
    lst = args[0]
    l = len(lst)

    s = sum(lst) % 3
    if s == 0:
        print(0)
    else:
        c = Counter(lst)
        if s == 1:
            if 1 in c:
                if l == 1:
                    print(-1)
                else:
                    print(1)
            elif 2 in c and c[2] >= 2:
                if l <= 2:
                    print(-1)
                else:
                    print(2)
            else:
                print(-1)
        else:   # s == 2
            if 2 in c:
                if l == 1:
                    print(-1)
                else:
                    print(1)
            elif 1 in c and c[1] >= 2:
                if l <= 2:
                    print(-1)
                else:
                    print(2)
            else:
                print(-1)
            

if __name__ == '__main__':
    args = [[int(i) % 3 for i in input()]]
    main(*args)
