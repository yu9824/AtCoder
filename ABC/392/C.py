def main(n: int, tup_p: tuple[int, ...], tup_q: tuple[int, ...]) -> None:
    tup_index_people = tuple(
        p for _, p in sorted((q, p) for q, p in zip(tup_q, tup_p))
    )
    """"ゼッケンをみたい番号の人の順番"""
    print(
        " ".join(
            map(
                str, (tup_q[index_people] for index_people in tup_index_people)
            )
        )
    )


if __name__ == "__main__":
    n = int(input())
    tup_p = tuple(map(lambda p: int(p) - 1, input().split()))  # 0-index化
    # tup_p = tuple(map(int, input().split()))  # 0-index化
    """見つめている人の番号"""
    tup_q = tuple(map(int, input().split()))
    """自分のゼッケン"""

    main(n, tup_p, tup_q)
