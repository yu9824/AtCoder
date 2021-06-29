def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

# imos法じゃ計算量的に解けないと気づくかどうか，それに対して工夫ができるかどうかがミソだった気がする．

# 解説通り
# https://atcoder.jp/contests/abc188/editorial/346
def main(*args):
    N, C, ABC = args

    # イベントを分解してc_i円かかるイベントがa_i日に起きる，c_i円安くなるイベントがb_i+1日に起きるというふうに考え，日付ごとにソート．（日付の左端を基準に考える．）
    event = []
    for a, b, c in ABC:
        event.extend([[a-1, c], [b, -c]])   # 0-indexに変換
    event.sort(key = lambda x:x[0])

    # 前回値段が変更された日付を保存しておくやつ
    the_day_before = 0
    # 今までにかかったコスト
    total_cost = 0
    # 現在1日あたりかかるコスト
    cost = 0
    # 値段が変更された瞬間，その前日までの費用を計算してtotal_costに加える．
    for day, diff_cost in event:
        if day != the_day_before:
            total_cost += (day - the_day_before) * min(C, cost)
            the_day_before = day
        cost += diff_cost

    print(total_cost)


if __name__ == '__main__':
    N, C = LI()
    args = [N, C]
    args.append([LI() for n in range(N)])

    main(*args)