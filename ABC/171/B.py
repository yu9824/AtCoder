# list(map(int, input().split()))
# int(input())

def main():
    N, K = list(map(int, input().split()))
    P = list(map(int, input().split()))

    P.sort()
    print(sum(P[:K]))

if __name__ == '__main__':
    main()
