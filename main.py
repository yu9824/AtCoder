# list(map(int, input().split()))
# int(input())

def main(N):
    if N == 1:
        print(input())
    else:
        # 小文字英字のリストを作成
        alpha = [chr(i) for i in range(97, 97+26)]

        # 何回出てきたかをカウントしておくリスト
        counta = [[0 for _ in range(26)] for __ in range(N)]

        for n in range(N):
            a = list(input())
            for s in a:
                counta[n][alpha.index(s)] += 1

        ans = []
        for n in range(N // 2):
            for i in range(26):
                # 上からn番目としたからn + 1番目両方に出てくるアルファベットがあるならば
                if counta[n][i] > 0 and counta[-(n + 1)][i] > 0:
                    ans[n:n] = [alpha[i], alpha[i]]
                    counta[n][i] -= 1
                    counta[-(n + 1)][i] -= 1
                    break
                elif i == 25:   # 一回も条件を満たすことなくここまできたら．
                    print(-1)
                    exit()
        if len(ans) + 1 == N:
            for i in range(26):
                if counta[N // 2][i] > 0:
                    ans.insert(N // 2, alpha[i])
                    break
        print(''.join(ans))


if __name__ == '__main__':
    N = int(input())
    main(N)
