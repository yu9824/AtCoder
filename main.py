# list(map(int, input().split()))
# int(input())

def main(N, s):
    # 0から9の鋳型を作成
    t = list('.###..#..###.###.#.#.###.###.###.###.###.')
    u = [[t[4*n+1:4*n+4]] for n in range(10)]
    lst = [list('.#.#.##....#...#.#.#.#...#.....#.#.#.#.#.'), list('.#.#..#..###.###.###.###.###...#.###.###.'), list('.#.#..#..#.....#...#...#.#.#...#.#.#...#.'), list('.###.###.###.###...#.###.###...#.###.###.')]
    for t in lst:
        for n in range(10):
            u[n].append(t[4*n+1:4*n+4])


    print(''.join([str(u.index(x)) for x in s]))








if __name__ == '__main__':
    N = int(input())
    for i in range(5):
        t = list(input())
        if i == 0:
            s = [[t[4*n+1:4*n+4]] for n in range(N)]
        else:
            for n in range(N):
                s[n].append(t[4*n+1:4*n+4])

    main(N, s)
