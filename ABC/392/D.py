from array import array
from collections import Counter
from itertools import combinations


def main(
    n: int, tup_k: tuple[int, ...], tup_dices: tuple[tuple[int, ...], ...]
) -> None:
    # len(tup_dices) == n
    _list_counters: list[Counter] = list()
    for _dice in tup_dices:
        _list_counters.append(Counter(_dice))

    p = 0.0
    """同じ目になる確率の最大値"""

    for i, j in combinations(range(n), 2):
        counter_i = _list_counters[i]
        counter_j = _list_counters[j]
        keys_common = set(counter_i) & set(counter_j)

        p = max(
            sum(counter_i[key] * counter_j[key] for key in keys_common)
            / (tup_k[i] * tup_k[j]),
            p,
        )
    else:
        print(p)


if __name__ == "__main__":
    n = int(input())
    _arr_k = array("i")
    _list_dices: list[tuple[int, ...]] = list()
    for _ in range(n):
        k, *a = map(int, input().split())
        _arr_k.append(k)
        _list_dices.append(tuple(a))

    main(n, tuple(_arr_k), tuple(_list_dices))
