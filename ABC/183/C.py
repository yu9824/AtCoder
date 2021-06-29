# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)

from itertools import permutations

def main(*args):
    N, K = args[:2]
    costs = args[2:]
    
    ans = 0
    for p in permutations([n for n in range(1, N)]):
        route = [0] + list(p) + [0]
        cost = 0
        for n in range(N):
            cost += costs[route[n]][route[n+1]]
        ans += cost == K
    print(ans)

if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    args = [N, K]
    for n in range(N):
        args.append(list(map(int, input().split())))
    main(*args)
