def main(N: int) -> None:
    grid = [[-1 for _ in range(N)] for _ in range(N)]
    # grid[N//2][N//2] = "T"
    y = 0
    """y座標"""
    x = -1
    """x座標"""
    i = 1
    """書き込んでいく数字"""

    def right(corr: tuple[int, int]) -> tuple[int, int]:
        return (corr[0] + 1, corr[1])

    def left(corr: tuple[int, int]) -> tuple[int, int]:
        return (corr[0] - 1, corr[1])

    def up(corr: tuple[int, int]) -> tuple[int, int]:
        return (corr[0], corr[1] + 1)

    def down(corr: tuple[int, int]) -> tuple[int, int]:
        return (corr[0], corr[1] - 1)

    n = N
    """n: 正方形のサイズ e.g.) 1, 3, 5, ..."""
    for _ in range(N // 2):
        for direction in (right, up, left, down):
            if direction.__name__ == "right":
                m = n
            elif direction.__name__ == "down":
                m = n - 2
            else:
                m = n - 1
            for _ in range(m):
                x, y = direction((x, y))
                # print(x, y)
                try:
                    grid[y][x] = i
                except IndexError as error:
                    print(grid)
                    raise error
                i += 1
        n -= 2

    # 最後に高橋くんを配置
    grid[N // 2][N // 2] = "T"
    for row in grid:
        print(*row)


if __name__ == "__main__":
    N = int(input())
    main(N)
