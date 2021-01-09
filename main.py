def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)
from collections import deque


def main(*args):
    N, AB, Q, TEX = args

    connects = [set() for n in range(N)]
    C = [0 for n in range(N)]
    for a, b in AB:
        connects[a-1].add(b-1)
        connects[b-1].add(a-1)
    
    depths = [-1 if n != 0 else 0 for n in range(N)]
    que = deque([0])
    
    while que:
        at = que.pop()
        for i in connects[at]:
            if depths[i] == -1:
                depths[i] = depths[at] + 1
                que.append(i)

    C = [0 for n in range(N)] 
    for t, e, x in TEX:
        a, b = AB[e-1]
        a -= 1
        b -= 1
        if depths[a] > depths[b]:
            a, b = b, a

        if t == 1:
            '''
            aから辿ってbを通らないすべて
            '''
            C[0] += x
            C[b] -= x
        else:   # t == 2
            '''
            bから辿ってaを通らないすべて
            '''
            C[b] += x

    que = deque([0])
    while que:
        at = que.pop()
        for i in connects[at]:
            if depths[at] < depths[i]:
                C[i] += C[at]
                que.append(i)
    
    {print(i) for i in C}



if __name__ == '__main__':
    N = int(input())
    args = [N]
    args.append([LI() for n in range(N-1)])
    Q = int(input())
    args.append(Q)
    args.append([LI() for q in range(Q)])
    main(*args)