import collections

def main(N, c):
    counta = [c.count(str(i + 1)) for i in range(4)]
    print(max(counta), min(counta))

if __name__ == '__main__':
    N = int(input())
    c = list(input())
    main(N, c)
