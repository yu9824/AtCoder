# list(map(int, input().split()))
# int(input())

# ****** PyPy3だったら通った． Pythonは落ちた ******
from collections import Counter

def main(H, W, M, obj_h, obj_w, obj):
    c_h = Counter(obj_h)
    c_w = Counter(obj_w)
    max_h = max(c_h.values())
    max_w = max(c_w.values())
    lst_h = [kv[0] for kv in c_h.items() if kv[1] == max_h]
    lst_w = [kv[0] for kv in c_w.items() if kv[1] == max_w]
    for h in lst_h:
        for w in lst_w:
            if (h, w) not in obj:
                print(max_h + max_w)
                exit()
    else:
        print(max_h + max_w - 1)



if __name__ == '__main__':
    H, W, M = list(map(int, input().split()))
    obj = set()
    obj_h = []
    obj_w = []
    for _ in range(M):
        i = list(map(int, input().split()))
        obj.add(tuple(i))
        obj_h.append(i[0])
        obj_w.append(i[1])
    main(H, W, M, obj_h, obj_w, obj)

# def main(H, W, Ch, Cw, Dh, Dw, S):
#
#
# if __name__ == '__main__':
#     # N = int(input())
#     # A = list(map(int, input().split()))
#     H, W = list(map(int, input().split()))
#     Ch, Cw = list(map(int, input().split()))
#     Dh, Dw = list(map(int, input().split()))
#     S = []
#     for _ in range(H):
#         S.append(input())
#     main(H, W, Ch, Cw, Dh, Dw, S)
