def main(x: int) -> None:
    for i in (1, 2, 3):
        if i == x:
            continue
        else:
            print(i)
            break


if __name__ == "__main__":
    x = int(input().strip())
    main(x)
