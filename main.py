def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
# 思ったこと
累積和かなぁ．いもす法っぽい．
'''

def main(*args):
    N, T, L, R = args
    max_R = max(R)
    imos = [0 for _ in range(max_R+1)]
    for t, l, r in zip(T, L, R):
        if t == 1:  # []
            imos[l-1] += 1
            imos[r] -= 1
        elif t == 2:    # [)
            imos[l-1] += 1
            imos[r-1] -= 1
        elif t == 3:    # (]
            imos[l] += 1
            imos[r] -= 1
        elif t == 4:
            imos[l] += 1
            imos[r-1] -= 1

    ruiseki = [0 for _ in range(max_R+1)]
    ruiseki[0] = imos[0]
    for i in range(1, max_R+1):
        ruiseki[i] = ruiseki[i-1] + imos[i]
    print(ruiseki, max(ruiseki))

    


if __name__ == '__main__':
    N = int(input())
    T = []
    L = []
    R = []
    for n in range(N):
        t, l, r = LI()
        T.append(t)
        L.append(l)
        R.append(r)
    main(N, T, L, R)

