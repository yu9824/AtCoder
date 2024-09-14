def main(ab, ac, bc):
    if ab == "<" and ac == "<":
        if bc == "<":
            print("B")
        else:
            print("C")
    elif ab == ">" and ac == ">":
        if bc == "<":
            print("C")
        else:
            print("B")
    elif ab == "<" and ac == ">":
        print("A")
    elif ab == ">" and ac == "<":
        print("A")


if __name__ == "__main__":
    ab, ac, bc = input().split()
    main(ab, ac, bc)
