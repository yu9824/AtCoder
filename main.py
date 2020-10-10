# list(map(int, input().split()))
# int(input())

def main(N, P):
    minimum = 0
    st = set()
    for p in P:
        if p != minimum:
            print(minimum)
            st.add(p)
        else:   # つまり p == minimum
            minimum += 1
            while minimum in st:
                st.remove(minimum)
                minimum += 1
            else:
                print(minimum)

if __name__ == '__main__':
    N = int(input())
    P = list(map(int, input().split()))
    main(N, P)
