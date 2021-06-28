# list(map(int, input().split()))
# int(input())

def main(N, A):
    div = 10 ** 9 + 7
    s = sum(A)
    ans = 0
    for a in A:
        s = s - a
        mult = ((s % div) * a) % div
        ans += mult
    print(ans % div)

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    main(N, A)
