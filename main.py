# list(map(int, input().split()))
# int(input())

# import sys
# sys.setrecursionlimit(10 ** 9)

from itertools import permutations

def main(*args):
    S = args[0]
    counts = [0 for n in range(10)]
    boolean = [False if n != 0 else True for n in range(10)]
    
    for s in S:
        int_s = int(s)
        if counts[int_s] < 3:
            counts[int_s] += 1
            if counts[int_s] == 3:
                boolean[int_s] = True
                if sum(boolean) == 10:
                    break

    l = []
    for i, c in enumerate(counts):
        l += [str(i)] * c
    
    S = l

    p = permutations(S, min(len(S), 3))
    for c in set(p):
        if int(''.join(c)) % 8 == 0:
            print('Yes')
            break
    else:
        print('No') 
    

if __name__ == '__main__':
    S = input()
    args = [S]
    main(*args)
