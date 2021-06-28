def main(N):
    # 対象の配列を作成
    A = [str(_ + 1) for _ in range(6)]

    # 最初の配列を保存
    start = A.copy()

    # 何回で一周するのかを求める．
    i = 0
    while A != start or i == 0:
        m = i % 5
        A[m], A[m + 1] = A[m + 1], A[m]
        i += 1

    # i回の操作で一周することがわかったので
    A = start.copy()    # 初期化
    for j in range(N % i):
        m = j % 5
        A[m], A[m + 1] = A[m + 1], A[m]
    print(''.join(A))


if __name__ == '__main__':
    N = int(input())
    main(N)
