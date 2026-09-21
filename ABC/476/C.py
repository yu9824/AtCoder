from collections import deque


def main(N: int, A: tuple[int, ...]) -> None:
    K = 3

    que = deque(A)

    s: list[int] = []
    for _ in range(K):
        s.append(que.popleft())

    s.sort(reverse=True)
    print(s[K - 1])

    for _ in range(N - K):
        s.append(que.popleft())
        s.sort(reverse=True)
        _ = s.pop(-1)
        print(s[-1])


if __name__ == "__main__":
    N = int(input().strip())
    A = tuple(map(int, input().strip().split()))

    main(N, A)
