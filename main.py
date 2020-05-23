# list(map(int, input().split()))
# int(input())

def main(N, M, Q, rinsetu, c):
    s = []
    for _ in range(Q):
        t = list(map(int, input().split()))
        if t[0] == 1:   # クエリ1(スプリンクラー起動)の場合
            x = t[1]
            # x番目のスプリンクラーの現在の色を出力
            print(c[x - 1])
            # x番目のスプリンクラーの色で隣接スプリンクラーの色を上塗り
            for r in rinsetu[x - 1]:
                c[r] = c[x - 1]
        else:   # クエリ2(色を上塗り)の場合
            x, y = t[1:]
            # x番目のスプリンクラーの現在の色を出力
            print(c[x - 1])
            # x番目のスプリンクラーの色を色yで上塗り
            c[x - 1] = y



if __name__ == '__main__':
    N, M, Q = list(map(int, input().split()))
    rinsetu = [[] for _ in range(N)]
    for _ in range(M):
        u, v = list(map(int, input().split()))
        rinsetu[u - 1].append(v - 1)
        rinsetu[v - 1].append(u - 1)
    c = list(map(int, input().split()))
    main(N, M, Q, rinsetu, c)
