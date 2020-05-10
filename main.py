# list(map(int, input().split()))
# int(input())


def main(S, T):
    if S == T[:-1]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    S = input()
    T = input()
    main(S, T)
