# list(map(int, input().split()))
# int(input())

import sys
sys.setrecursionlimit(10 ** 9)


# '{:.7f}'.format(i)

# def main(*args):
#     A, B, C = sorted(args)  # Cが一番大きい
#     s = A + B + C
#     P = (A / s, B / s, C / s)
#     print(100 - C, '回から', 300 - s - 2, '回までに終わる．')

#     ans = 0
#     for j in range(100-C, 300 - s - 2 + 1):
#         ans += P[2] * (100 - C)
#         ans += P[1] * (100 - C - )

    # print(((100 - A) * A + (100 - B) * B + (100 - C) * C) / s)
    
    # def cal(A, j):
    #     return (A + j) / (s + j)

    # def get_sum(A):
    #     return sum(map(cal, [A] * (100 - A), range(0, 100-A)))
    # a = get_sum(A)
    # b = get_sum(B)
    # c = get_sum(C)
    # print('{:.7f}'.format(a + b + c))
    
    

# if __name__ == '__main__':
#     args = list(map(int, input().split()))
#     main(*args)





def main(*args):
    r1, c1, r2, c2 = args

    # 原点移動させて考える
    now = [r2 - r1, c2 - c1]
    if now == [0, 0]:
        cnt = 0
    elif abs(now[0]) <= 3 and abs(now[1]) <= 3 and abs(now[0]) + abs(now[1]) <= 3:
        cnt = 1
    else:
        if abs(now[0] - now[1]) == 0 or abs(now[0] + now[1]) == 0:
            cnt = 1
        elif abs(now[0] - now[1]) <= 3 or abs(now[0] + now[1]) <= 3:
            cnt = 2
        elif sum(now) % 2 == 0:
            cnt = 2
        else:
            cnt = 3
    print(cnt)
    

if __name__ == '__main__':
    args = list(map(int, input().split())) + list(map(int, input().split()))
    main(*args)
    