def main(a_0: int, a_1: int, a_2: int) -> None:
    if a_0 * a_1 == a_2:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    tup_a = tuple(sorted(map(int, input().split())))
    main(*tup_a)
