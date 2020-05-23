# list(map(int, input().split()))
# int(input())
def main(s, t):
    if s == t:
        print('same')
    elif s.upper() == t.upper():
        print('case-insensitive')
    else:
        print('different')


if __name__ == '__main__':
    s = input()
    t = input()
    main(s, t)
