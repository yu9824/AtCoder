# list(map(int, input().split()))
# int(input())

'''
PythonだとTLE
PyPyでも一つだけ (random_05.txtだけTLE)だけどこれ以上高速化する方法がわからない．
'''

def main(H, W, C, D, S):
    def inside(x, y):
        return ((0 <= x and x < H) and (0 <= y and y < W))

    next = {C}
    masu = [[-1 for _ in range(W)] for __ in range(H)]

    def moverange(x, y):
        return inside(x, y) and masu[x][y] == -1 and S[x][y] == '.'

    def func(now, kaisu):
        x, y = now
        for canmove in {(x-1, y), (x+1, y), (x, y+1), (x, y-1)}:
            if moverange(*canmove):
                que.add(canmove)
                masu[canmove[0]][canmove[1]] = kaisu

    def make_st(x, y):
        return {(x+i, y+j) for i in range(-2, 3) for j in range(-2, 3)}

    kaisu = -1
    while len(next) != 0:
        kaisu += 1
        que = next
        next = set()
        while que:
            now = que.pop()
            if moverange(*now):
                masu[now[0]][now[1]] = kaisu
            func(now, kaisu)

            for canmove in make_st(*now):
                if moverange(*canmove):
                    next.add(canmove)
    print(masu[D[0]][D[1]])


if __name__ == '__main__':
    H, W = list(map(int, input().split()))
    C = tuple(map(lambda x:int(x)-1, input().split()))
    D = tuple(map(lambda x:int(x)-1, input().split()))
    S = [input() for _ in range(H)]
    main(H, W, C, D, S)
