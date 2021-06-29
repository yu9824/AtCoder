# list(map(int, input().split()))
# int(input())

def main():
    N = input()

    s = 0
    for n in N:
        s += int(n)
    if s % 9 == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
