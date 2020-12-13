# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)


def main(*args):
    N, M, T, AB = args

    battery = N
    before = 0  # 前カフェにいた時間．(初期値は0，満タンのため．)
    for A, B in AB: # 最後のカフェを出る瞬間まで
        decrease = A - before
        increase = B - A
        if decrease >= battery: # 充電切れたら終わり．
            print('No')
            break

        # 結局この一本の式でOK
        battery = min(battery + increase - decrease, N) # 最大容量は超えられない．
        # if decrease > increase:  # 減少分の方が大きい
        #     battery -= (decrease - increase)
        # else:   # 増加分の方が大きい or 等しい
        #     battery = min(battery + increase - decrease, N) # 最大容量は超えられない．
                
        # beforeの更新
        before = B
        
    else:   # 最後のカフェを出てから帰るまで
        battery -= (T - before)
        if battery > 0:
            print('Yes')
        else:
            print('No')   
    

if __name__ == '__main__':
    N, M, T = list(map(int, input().split()))
    args = [N, M, T]
    args.append([list(map(int, input().split())) for m in range(M)])
    main(*args)