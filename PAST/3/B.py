# list(map(int, input().split()))
# int(input())
import numpy as np

def main(N, M, Q):
    # 正解その問題の配点
    haiten = np.ones(M, dtype = int) * N

    # 正解したかどうかの行列
    array = np.zeros([N, M], dtype = int)

    for _ in range(Q):
        s = list(map(int, input().split()))
        if s[0] == 2:
            n = s[1]
            m = s[2]
            array[n - 1][m - 1] = 1
            haiten[m - 1] -= 1
        else:
            n = s[1]
            print(array[n - 1] @ haiten)


if __name__ == '__main__':
    N, M, Q = list(map(int, input().split()))
    main(N, M, Q)
