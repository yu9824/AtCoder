# list(map(int, input().split()))
# int(input())
def main(A, V, B, W, T):
    dist = abs(A - B)
    velo = V - W
    if dist <= velo * T:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    A, V = list(map(int, input().split()))
    B, W = list(map(int, input().split()))
    T = int(input())
    main(A, V, B, W, T)
