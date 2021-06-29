# list(map(int, input().split()))
# int(input())

from decimal import Decimal

def main():
    N = int(input())
    X = list(map(int, input().split()))
    abs_X = tuple(map(abs, X))
    sqrt_X = tuple(map(lambda x:x ** 2, X))
    m = sum(abs_X)
    e = Decimal(str(sum(sqrt_X))) ** Decimal('0.5')
    c = max(abs_X)
    print(m)
    print(e)
    print(c)

if __name__ == '__main__':
    main()