def main(N, P):
    maximum = 0
    for i in range(N):
        for j in range(i, N):
            maximum = max(maximum, d(P[i], P[j]))
    print('{:.04f}'.format(maximum))

def d(p, q):
    return ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** 0.5

if __name__ == '__main__':
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    main(N, P)
