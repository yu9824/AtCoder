# list(map(int, input().split()))
# int(input())
import numpy as np
from numba import njit


def main():
    lst = list(map(int, input().split()))
    for i, l in enumerate(lst):
        if l == 0:
            print(i + 1)
            exit()

if __name__ == '__main__':
    main()
