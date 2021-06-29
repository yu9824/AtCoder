def main(a, b, c):
    for i in range(1, 128):
        if i % 3 == a and i % 5 == b and i % 7 == c:
            print(i)

if __name__ == '__main__':
    a, b, c = list(map(int, input().split()))
    main(a, b, c)
