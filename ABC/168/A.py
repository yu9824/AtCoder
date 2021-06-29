# list(map(int, input().split()))
# int(input())

def main(N):
    a = N % 10
    if a in [2, 4, 5, 7, 9]:
        print('hon')
    elif a == 3:
        print('bon')
    else:
        print('pon')


if __name__ == '__main__':
    N = int(input())
    main(N)
