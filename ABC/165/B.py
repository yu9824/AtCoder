def main(X):
    year = 0
    money = 100
    while X > money:
        money = int(money * 1.01)
        year += 1
    print(year)

if __name__ == '__main__':
    X = int(input())
    main(X)
