def main(n: int, m: int, tup_a: tuple[int, ...]) -> None:
    st_n = set(range(1, n + 1))
    st_not_included = st_n - set(tup_a)
    print(c := len(st_not_included))
    print(" ".join(map(str, sorted(st_not_included))))


if __name__ == "__main__":
    n, m = map(int, input().split())
    tup_a = tuple(map(int, input().split()))

    main(n, m, tup_a)
