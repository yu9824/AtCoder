from collections import deque


def main(n: int, tup_a: tuple[int, ...]):
    balls = deque((-999,))
    for i_iter in range(n):
        balls.append(tup_a[i_iter])
        while balls[-2] == balls[-1]:
            balls.pop()
            balls.append(balls.pop() + 1)
        # if len(balls) < 2:  # 手順1
        #     continue
        # elif balls[-2] != balls[-1]:  # 手順2
        #     continue
        # else:  # 手順3
        #     balls.pop()
        #     balls.append(balls.pop() + 1)
    print(len(balls) - 1)


if __name__ == "__main__":
    n = int(input())
    tup_a = tuple(map(int, input().split()))

    main(n, tup_a)
