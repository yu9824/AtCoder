# list(map(int, input().split()))
# int(input())

def main():
    N = int(input())
    L = sorted(list(map(int, input().split())))

    cnt = 0
    for i, x in enumerate(L[:-2]):
        for j, y in enumerate(L[i+1:-1]):
            for z in L[i+j+2:]:
                if len({x, y, z}) == 3:
                    cnt += int(x + y > z)
    print(cnt)

if __name__ == '__main__':
    main()
