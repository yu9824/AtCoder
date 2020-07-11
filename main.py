# list(map(int, input().split()))
# int(input())

def main(N, X):
    lst = list(map(int, list(X)))
    num = lst.count(1)  # 初期状態で1を持つ数．

    def func(x):    # xは10進数
        lst = list(bin(x)[2:])
        amari =  x % lst.count('1')
        return amari

    d = {}
    for i in range(1, N):
        d[i] = func(i)


    # 反転させるので num + 1 か， num - 1 で割る場合しか存在しない．
    plus = []   # num + 1 で各桁 (2 ** n) を割った値を保存
    minus = []  # num - 1 で各桁 (2 ** n) を割った値を保存

    p = 1
    m = 1
    for n in range(N):
        p %= (num + 1)
        plus.append(p)
        p *= 2
        if num - 1 > 0:
            m %= (num - 1)
            minus.append(m)
            m *= 2

    o = int(X, 2)   # originalの 'o'
    amari_plus = o % (num + 1)
    if num - 1 > 0:
        amari_minus = o % (num - 1)

    for i in range(N):
        if lst[i] == 0:
            amari = (amari_plus + plus[- i - 1]) % (num + 1)
        elif num - 1 <= 0:
            print(0)
            continue
        else:
            amari = (amari_minus + (num - 1) - minus[- i - 1]) % (num - 1)
        ans = 1
        while amari != 0:
            amari = d[amari]
            ans += 1
        print(ans)

if __name__ == '__main__':
    N = int(input())
    X = input()

    # N = 2 * 10 ** 5
    # import numpy as np
    # X = ''.join([str(int(round(i))) for i in np.random.rand(N)])

    # N = 3
    # X = '100'

    # import time
    # t1 = time.time()
    main(N, X)
    # t2 = time.time()
    # print(t2 - t1)
