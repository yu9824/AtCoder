def main(S):
    loc_b: list = []
    loc_r: list = []
    loc_k: int = 0
    for i in range(8):
        s = S[i]
        if s == "B":
            loc_b.append(i)
        elif s == "K":
            loc_k = i
        elif s == "R":
            loc_r.append(i)
    if loc_r[0] < loc_k < loc_r[1] and loc_b[0] % 2 != loc_b[1] % 2:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    S = input()
    main(S)
