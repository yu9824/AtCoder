import collections

def main(N, A):
    c = collections.Counter(A)
    [print(c[i+1]) for i in range(max(c.keys()))]
    [print(0) for i in range(max(c.keys()), N)]

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    # N = 7
    # A = list(map(int, "1 2 3 4 5 6".split()))
    main(N, A)
