# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)

def main(*args):
    N, AB = args

    ruiseki = []
    for a, b in AB:
        ruiseki.extend([- ((a - 1) * a) // 2, (b * (b + 1)) // 2])
    print(sum(ruiseki))

    

if __name__ == '__main__':
    N = int(input())
    args = [N]
    args.append([tuple(map(int, input().split())) for n in range(N)])
    main(*args)
    