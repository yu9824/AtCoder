# list(map(int, input().split()))
# int(input())

def main(*args):
    X, Y, A, B = args   # *A, +B
    
    # 何回までは倍，倍にして行った方が効率がよいのかの境目を求める．
    border = 0
    while X < Y:
        add = X * (A-1)
        if add < B: # Bを加えるよりも小さくて済む場合
            X += add
            border += 1
        else:
            keikenchi = border + ((Y - 1) - X) // B
            break
    else:   # 途中で超えちゃったとき．
        keikenchi = border - 1
    print(keikenchi)

if __name__ == '__main__':
    args = list(map(int, input().split()))
    main(*args)