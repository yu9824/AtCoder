def main(grid_a, grid_b):
    for i in range(n):
        for j in range(n):
            if grid_a[i][j] != grid_b[i][j]:
                print(i + 1, j + 1)
                exit()


if __name__ == "__main__":
    n = int(input())
    grid_a = tuple(input() for _ in range(n))
    grid_b = tuple(input() for _ in range(n))
    main(grid_a, grid_b)
