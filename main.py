def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

from collections import deque

# http://prdc.hatenablog.com/entry/2017/09/12/124845
# http://algorithms.blog55.fc2.com/blog-entry-132.html

def main(*args):
    N, A = args
    A += [0]

    # ヒストグラムと考えた (左端位置, 高さ) を追加していく
    que = deque()
    result = 0
    
    for r, a in enumerate(A):
        if que: # queに何か入っていたら
            b = que[-1][1]
            if a > b:
                que.append([r, a])
            elif a < b:
                while a <= que[-1][1]:
                    l, b = que.pop()
                    result = max(result, (r - l) * b)
                    if not que:
                        break
                # 最後にqueから取り出した左端位置を使って追加，
                que.append([l, a])
        else:   # queが空だったら
            que.append([r, a])
            
    print(result)

    

if __name__ == '__main__':
    N = int(input())
    args = [N]
    args.append(LI())
    
    # N = 6
    # A = [1, 3, 3, 5, 7, 2]
    # args = [N, A]

    # import numpy as np
    # N = 10 ** 4
    # A = np.random.randint(1, 10 ** 5 + 1, N).tolist()
    # args = [N, A]

    main(*args)