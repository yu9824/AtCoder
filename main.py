# list(map(int, input().split()))
# int(input())

def main(N, C):
    counta_R = 0
    counta_W = 0
    for i, c in enumerate(C):
        if c == 'R':
            counta_R += 1
        else:
            counta_W += 1
    if counta_R == 0 or counta_W == 0:
        print(0)
        exit()
    ideal = 'R' * counta_R + 'W' * counta_W
    print(C.count('W', 0, counta_R))


if __name__ == '__main__':
    N = int(input())
    C = input()
    main(N, C)
