# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)

from math import sqrt, floor, ceil

def get_sieve_of_eratosthenes(n):
    # 変数定義
    prime = [2]
    limit = int(n**0.5)

    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    elif n == 2:
        return prime
    
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]

def factorization(n, p):
    arr = []
    temp = n
    for i in p:
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr


def main(*args):
    N = args[0]

    # 素数列挙
    ps = get_sieve_of_eratosthenes(N)

    # 素数の最大個数を保存しておく辞書
    d = dict(zip(ps, [0 for _ in range(len(ps))]))

    for n in range(2, N+1):
        for p, x in factorization(n, ps):   # p: 素数の種類, x:その素数が含まれる個数
            d[p] = max(d[p], x)
    
    ans = 1
    for p, x in d.items():
        ans *= p ** x

    return ans + 1
    

if __name__ == '__main__':
    args = [int(input())]
    ans = main(*args)
    print(ans)