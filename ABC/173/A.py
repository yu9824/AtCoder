# list(map(int, input().split()))
# int(input())

def main():
    N = int(input())
    amari = N % 1000 if N % 1000 else 1000
    print(1000 - amari)

if __name__ == '__main__':
    main()
