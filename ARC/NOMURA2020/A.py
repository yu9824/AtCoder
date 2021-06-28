# list(map(int, input().split()))
# int(input())

def main():
    H1, M1, H2, M2, K = list(map(int, input().split()))
    t1 = H1 * 60 + M1
    t2 = H2 * 60 + M2
    print(t2 - t1 - K)



if __name__ == '__main__':
    main()
