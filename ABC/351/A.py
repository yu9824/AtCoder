def main(tup_a, tup_b):
    print(sum(tup_a) - sum(tup_b) + 1)


if __name__ == "__main__":
    tup_a = tuple(map(int, input().split()))
    tup_b = tuple(map(int, input().split()))
    main(tup_a, tup_b)
