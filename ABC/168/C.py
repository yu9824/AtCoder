# list(map(int, input().split()))
# int(input())
from math import cos, pi

def main(A, B, H, M):
    theta_b = M / 60 * (2 * pi)
    theta_a = 1 / 12 * (H + M / 60) * (2 * pi)
    AB = (A ** 2 + B ** 2 - 2 * A * B * cos(theta_a - theta_b)) ** 0.5
    print(AB)

if __name__ == '__main__':
    A, B, H, M = map(int, input().split())
    main(A, B, H, M)
