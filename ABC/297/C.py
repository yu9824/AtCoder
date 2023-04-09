def main(H: int, W: int, S: str):
    new_S = []
    h = 0
    while h < H:
        w = 0
        while w < W:
            if w == W - 1:
                new_S.append(S[h][w])
                w += 1
            elif S[h][w] == "T" and S[h][w + 1] == "T":
                new_S.append("P")
                new_S.append("C")
                w += 2
            else:
                new_S.append(S[h][w])
                w += 1
        else:
            h += 1
    {print("".join(new_S)[W * h : w * (h + 1)]) for h in range(H)}


if __name__ == "__main__":
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    main(H, W, S)
