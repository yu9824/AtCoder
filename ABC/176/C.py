# list(map(int, input().split()))
# int(input())

def main(N, A):
    b = A.pop(0)

    l = 0
    for a in A:
        if a > b:
            b = a
        else:
            l += b - a
    print(l)

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    main(N, A)
