def main(N: int, S: str, T: str) -> None:
    for i in range(N):
        if T[i] == "*" or S[i] == T[i]:
            continue
        else:
            print("No")
            break
    else:
        print("Yes")


if __name__ == "__main__":
    N = int(input().strip())
    S = input().strip()
    T = input().strip()
    main(N, S, T)
