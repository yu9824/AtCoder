# list(map(int, input().split()))
# int(input())

def main():
    N, D = list(map(int, input().split()))
    counta = 0
    D_2 = D ** 2
    for _ in range(N):
        x, y = list(map(int, input().split()))
        if x ** 2 + y ** 2 <= D_2:
            counta += 1
    print(counta)

if __name__ == '__main__':
    main()
