def main(N: int, Q: int, queryies: list):
    corrs = list(zip(range(N, 0, -1), [0] * N))
    for query in queryies:
        mode, command = query
        if mode == "1":
            corr_head = corrs[-1]
            if command == "R":

                def f(x):
                    return (x[0] + 1, x[1])

            elif command == "L":

                def f(x):
                    return (x[0] - 1, x[1])

            elif command == "U":

                def f(x):
                    return (x[0], x[1] + 1)

            elif command == "D":

                def f(x):
                    return (x[0], x[1] - 1)

            corrs += [f(corr_head)]
        elif mode == "2":
            index = -int(command)
            print(*corrs[index])


if __name__ == "__main__":
    N, Q = map(int, input().split())
    queryies = [input().split() for _ in range(Q)]
    main(N, Q, queryies)


# 下記が遅すぎて通んなかったやつ2つ
"""
from copy import copy


def main(N: int, Q: int, queryies: list):
    corrs = list(map(list, zip(range(1, N + 1), [0] * N)))
    for query in queryies:
        mode, command = query
        if mode == "1":
            corr_head = copy(corrs[0])
            if command == "R":
                corr_head[0] += 1
                corrs = [corr_head] + corrs[:-1]
            elif command == "L":
                corr_head[0] -= 1
                corrs = [corr_head] + corrs[:-1]
            elif command == "U":
                corr_head[1] += 1
                corrs = [corr_head] + corrs[:-1]
            elif command == "D":
                corr_head[1] -= 1
                corrs = [corr_head] + corrs[:-1]
        elif mode == "2":
            print(corrs[int(command) - 1][0], corrs[int(command) - 1][1])


if __name__ == "__main__":
    N, Q = map(int, input().split())
    queryies = [input().split() for _ in range(Q)]
    main(N, Q, queryies)

"""


"""
def main(N: int, Q: int, queryies: list):
    corrs = list(zip(range(1, N + 1), [0] * N))
    for query in queryies:
        mode, command = query
        if mode == "1":
            if command == "R":
                corrs = [(corrs[0][0] + 1, corrs[0][1])] + corrs[:-1]
            elif command == "L":
                corrs = [(corrs[0][0] - 1, corrs[0][1])] + corrs[:-1]
            elif command == "U":
                corrs = [(corrs[0][0], corrs[0][1] + 1)] + corrs[:-1]
            elif command == "D":
                corrs = [(corrs[0][0], corrs[0][1] - 1)] + corrs[:-1]
        elif mode == "2":
            print(corrs[int(command) - 1][0], corrs[int(command) - 1][1])


if __name__ == "__main__":
    N, Q = map(int, input().split())
    queryies = [input().split() for _ in range(Q)]
    main(N, Q, queryies)

"""
