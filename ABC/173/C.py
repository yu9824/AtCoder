# list(map(int, input().split()))
# int(input())
from itertools import combinations

def main(H, W, K, HW):
    ans = 0

    # もとのHWに含まれる黒の数を数える．
    n_all = sum(HW, []).count('#')

    # 組み合わせ生成
    comb_h = []
    comb_w = []
    for h in range(H):
        comb_h.extend(combinations([i for i in range(H)], h))
    for w in range(W):
        comb_w.extend(combinations([i for i in range(W)], w))

    # h行目にある黒の数を数える．
    for c_h in comb_h:
        n_h = 0
        for h in c_h:
            n_h += HW[h].count('#')

        # w行目にある黒の数を数える．
        for c_w in comb_w:
            n_w = 0
            n_hw = 0
            for w in c_w:
                for h in range(H):
                    if HW[h][w] == '#':
                        n_w += 1
                        if h in c_h:
                            n_hw += 1
            # print(c_h, c_w, n_h, n_w, n_hw)
            n_black = n_all - n_h - n_w + n_hw
            if n_black == K:
                ans += 1
    print(ans)

if __name__ == '__main__':
    H, W, K = list(map(int, input().split()))
    HW = []
    for h in range(H):
        HW.append(list(input()))
    main(H, W, K, HW)
