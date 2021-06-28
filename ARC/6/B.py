def main(N, L, x, o):
    '''
    lは一段目を0, 二段目を1
    nは一列目を0, 二列目を2...としてる．
    '''
    # 初期条件 (oは読み取った時からpython基準なので変換不要)
    n = o

    for l in range(L - 1, -1, -1):  # あたり (下) から上へ遡る
        if OK(n - 1) and x[l][n - 1] == '-':  # 左があみだをはみでないで，かつ横道があるなら
            n -= 2  # 左の列へ移動
        elif OK(n + 1) and x[l][n + 1] == '-':  # 右があみだをはみでないで，かつ横道があるなら
            n += 2  # 右の列へ移動

    print(n // 2 + 1)   # nは一列目を0, 二列目を2...としてる．→1, 2, 3, ...に変換

def OK(n):
    return 0 <= n and n <= 2 * N - 2


if __name__ == '__main__':
    N, L = list(map(int, input().split()))
    x = [list(input()) for _ in range(L)]
    o = list(input()).index('o')
    main(N, L, x, o)
