# list(map(int, input().split()))
# int(input())
import itertools

def main(N, M, X, CA):
    cand = []
    for n in range(N):  # n個選ぶ
        for ca in itertools.combinations(CA, n+1):
            s, price = f(ca)
            if all(i >= X for i in s):
                cand.append(price)
    if len(cand) == 0:
        print(-1)
    else:
        print(min(cand))


def f(lst):
    s = [0 for _ in range(M)]
    price = 0
    for ca in lst:
        price += ca[0]
        for i in range(M):
            s[i] += ca[i+1]
    return s, price





if __name__ == '__main__':
    N, M, X = list(map(int, input().split()))
    CA = []
    for _ in range(N):
        CA.append(list(map(int, input().split())))

    main(N, M, X, CA)
