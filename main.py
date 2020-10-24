# list(map(int, input().split()))
# int(input())

# def main(*args):
#     def cost(city1, city2):
#         return abs(city2[0] - city1[0]) + abs(city2[1] - city1[1]) + max(0, city2[2] - city1[2])
    
#     N, cities = args
#     # S = {n for n in range(N)}
#     S = 2 ** (N-1) - 1

#     costs = [[cost(city1, city2) if city1 != city2 else float('inf') for city2 in cities] for city1 in cities]

#     memo = {}
#     def TSP_DP(a, S, b):
#         # S = S - {a}
#         S = S - 2 ** a
#         # if len(S) == 0:
#         if S == 0:
#             # memo[(a, tuple(S), b)] = costs[a][b]
#             memo[(a, S, b)] = costs[a][b]
#             return costs[a][b]
        
#         # if (a, tuple(S), b) in memo:
#         if (a, S, b) in memo:
#             # return memo[(a, tuple(S), b)]
#             return memo[(a, S, b)]
        
#         # c_min = min([costs[a][s] +  TSP_DP(s, S - {s}, b) for s in S])
#         c_min = min([costs[a][n] +  TSP_DP(n, S - (2 ** n), b) for n in range(N) if (S >> n) & 1])
#         # memo[(a, tuple(S), b)] = c_min
#         memo[(a, S, b)] = c_min
#         return c_min

#     print(TSP_DP(0, S, 0))
        
    

# if __name__ == '__main__':
#     N = int(input())
#     cities = []
#     for n in range(N):
#         cities.append(tuple(map(int, input().split())))
#     args = N, cities
#     main(*args)



from math import log, ceil
from decimal import Decimal, ROUND_HALF_UP
def main(N):
    st = {3 ** i for i in range(1, ceil(log(10 ** 18, 3)))}
    b = ceil(log(N, 5))    # ここで不動小数点でバグり散らかしてたのでとりあえず絶対一番上の数が含まれるようにする．


    while b > 0:
        # print(b)
        memo = N - 5 ** b
        # if memo > 0:
        #     a = log(memo, 3)
        # else:
        #     b -= 1
            # continue
        if memo in st:
        # if a != 0 and a == int(a):  # 多分ここの丸めこみで死んでる．
            a = Decimal(log(memo, 3)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
            print(a, b)
            break
        else:
            b -= 1
    else:
        print(-1)

N = int(input())
main(N)

# for i in range(1, 10 ** 18):
#     if type(main(i)) == tuple:
#         a, b = main(i)
#         print(i, (a, b))
    