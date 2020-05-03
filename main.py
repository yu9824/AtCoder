import math

def main(X):
    lst = f(X)
    for L in lst:
        for l in L:
            for B in range(-120, 120, 1):
                A = B + l[0]
                if g(A, B):
                    print(A, B)
                    exit()

def f(X):
    return [[[X // i, i], [i, X // i]] for i in range(1, math.floor(X ** 0.5) + 1) if X % i == 0]

def g(A, B):
    return A ** 5 - B ** 5 == X



if __name__ == '__main__':
    X = int(input())
    main(X)
