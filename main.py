N, M = list(map(int, input().split()))
disk = [int(input()) for _ in range(M)]

CD = [i for i in range(N + 1)]  # それぞれのdiskに入ってるCDの番号 0に入ってる = CDプレイヤーに入ってる

for i in disk:  #次聞くやつ
    l = CD.index(i)
    CD[0], CD[l] = CD[l], CD[0]
[print(CD[i + 1]) for i in range(N)]
