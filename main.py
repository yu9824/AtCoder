# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)

from collections import deque

def main(*args):
    N, S = args

    counta = 0  # 何個の 'fox' があったか
    active = deque()    # activeな'f', 'o'があるかを保存しておくque
    for n in range(N):
        # print(active)
        if S[n] == 'f':
            active.append('f')
            continue
        elif len(active) == 0:
            pass
        elif S[n] == 'o':
            if active[-1] == 'f':
                active.append('o')
                continue
        elif S[n] == 'x':
            if active[-1] == 'o':
                active.pop()
                active.pop()
                counta += 1
                continue
        active.clear()
    print(N - counta * 3)


if __name__ == '__main__':
    args = [int(input()), input()]
    main(*args)
