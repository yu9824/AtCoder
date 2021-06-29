# list(map(int, input().split()))
# int(input())

from collections import deque

def main(N, A):
    # 席順
    l = A[:2]
    # 心地よさ合計
    ans = A[0]

    d = deque([A[1], A[1]])

    for a in A[2:]:
        ans += d.popleft()
        d.extend([a, a])
    print(ans)



if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    # import numpy as np
    # N = 2
    # A = list(np.arange(N, dtype = int) + 1)


    # import time
    # import numpy as np
    # N = 10 ** 5
    # A = list((np.random.rand(N) * 10 ** 9).astype(int))
    #
    # print('生成完了！')
    # t1 = time.time()
    A.sort(reverse = True)
    main(N, A)
    # t2 = time.time()
    # print(t2 - t1)
