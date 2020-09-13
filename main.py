# list(map(int, input().split()))
# int(input())

# 余事象と見れなかった時点で絶望的

mod = 10 ** 9 + 7
def main(N):
    print((10 ** N - (9 ** N) * 2 + (8 ** N)) % mod)


if __name__ == '__main__':
    N = int(input())
    main(N)
