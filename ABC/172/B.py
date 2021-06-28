# list(map(int, input().split()))
# int(input())

def main(S, T):
    ans = 0
    for s, t in zip(S, T):
        ans += s != t
    print(ans)


if __name__ == '__main__':
    S = list(input())
    T = list(input())
    main(S, T)
