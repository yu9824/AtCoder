# list(map(int, input().split()))
# int(input())

def main():
    D, T, S = list(map(int, input().split()))
    if D <= T * S:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
