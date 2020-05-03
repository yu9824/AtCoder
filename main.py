import math

def main(A, B, N):
    x = min(B-1, N)
    answer = math.floor(A * x / B) - A * math.floor(x / B)
    print(answer)

if __name__ == '__main__':
    A, B, N = list(map(int, input().split()))
    main(A, B, N)
