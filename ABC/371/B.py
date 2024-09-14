from array import array


def main(n: int, m: int, arr_a: array, list_b: list):
    arr_taro = array("B", (1,) * n)
    for a, b in zip(arr_a, list_b):
        if arr_taro[a] and b == "M":
            print("Yes")
            arr_taro[a] = False
        else:
            print("No")


if __name__ == "__main__":
    n, m = map(int, input().split())

    arr_a = array("I")
    list_b = list()
    for _ in range(m):
        _a, _b = input().split()
        arr_a.append(int(_a) - 1)  # 1-index to 0-index
        list_b.append(_b)
    main(n, m, arr_a, list_b)
