def main(b, a):
    dict_change = {str(x):str(i) for i, x in enumerate(b)}
    dict_reverse = {str(i):str(x) for i, x in enumerate(b)}
    A = list(map(str, sorted([int(j.translate(str.maketrans(dict_change))) for i, j in enumerate(a)])))
    [print(int(j.translate(str.maketrans(dict_reverse)))) for i, j in enumerate(A)]


if __name__ == '__main__':
    b = list(map(int, input().split()))
    N = int(input())
    a = [input() for _ in range(N)]
    main(b, a)
