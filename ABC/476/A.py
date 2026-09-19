def main(S: str) -> None:
    if S.endswith("e"):
        print(S + "r")
    else:
        print(S + "er")


if __name__ == "__main__":
    S = input().strip()
    main(S)
