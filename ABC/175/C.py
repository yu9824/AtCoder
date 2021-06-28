# list(map(int, input().split()))
# int(input())

def main(X, K, D):
    x = abs(X)
    k = K

    shou, amari = x // D, x % D
    if shou >= k:   # 0付近までたどり着かないとき
        x -= k * D
        k = 0
    else:
        k -= (shou + 1)
        x -= (shou + 1) * D

    if k % 2:    # 奇数のとき
        print(abs(x + D))
    else:   # 偶数の時
        print(abs(x))

if __name__ == '__main__':
    X, K, D = list(map(int, input().split()))
    main(X, K, D)
