# list(map(int, input().split()))
# int(input())

def main(N):
    A = list(map(int, input().split()))
    st_A = set(A)
    if 0 in st_A:
        print(0)
    else:
        x = 1
        for a in A:
            x *= a
            if x > 10 ** 18:
                print(-1)
                exit()
        else:
            print(x)





if __name__ == '__main__':
    N = int(input())
    main(N)
