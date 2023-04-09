def main(A, B):
    cnt = 0
    # Bのほうが大きい
    A, B = sorted([A, B])
    while A > 1 and B % A:
        cnt += B // A
        A, B = B % A, A
    else:
        if A == 1:
            cnt += B - 1
        else:   # BがAで割り切れるとき
            cnt += B // A - 1
    print(cnt)


if __name__ == "__main__":
    A, B = map(int, input().split())
    main(A, B)
