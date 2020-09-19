# list(map(int, input().split()))
# int(input())

def main():
    S = input()
    if S[-1] == 's':
        print(S + 'es')
    else:
        print(S + 's')

if __name__ == '__main__':
    main()
