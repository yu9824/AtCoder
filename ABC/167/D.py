# list(map(int, input().split()))
# int(input())

def main(N, K, A):
    i = 0   # 現在地
    lst_memo = []
    set_memo = set([])
    while i not in set_memo:
        lst_memo.append(i)
        set_memo.add(i)
        i = A[i] - 1    # pythonは一つずれる
    key = lst_memo.index(i)
    if K < key:
        print(lst_memo[K] + 1)
    else:
        roop = lst_memo[key:]
        print(roop[(K - key) % len(roop)] + 1)    # pythonは一つずれる


if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    main(N, K, A)
