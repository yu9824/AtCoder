# list(map(int, input().split()))
# int(input())


'''
PyPyならギリギリ通った
pythonだと4~5秒でTLE

・集合(set)→bit
・costsの算出を(N × N)→ (N × N / 2)
をしたことでギリギリ通るようになった．

PyPyでなくpythonで通しててギリ自分でも書けそうな人のコード: https://atcoder.jp/contests/abc180/submissions/17477652
ただ，どうしてここまで実行時間に差がついたのかがどうしてもわからない．
'''

import sys
sys.setrecursionlimit(10 ** 9)

def main(*args):
    N, cities = args

    # def cost(city1, city2):
    #     return abs(city2[0] - city1[0]) + abs(city2[1] - city1[1]) + max(0, city2[2] - city1[2])
    # costs = [[cost(city1, city2) if city1 != city2 else float('inf') for city2 in cities] for city1 in cities]    # これもメモ再帰化しないと間に合わなそう．
    
    costs = [[float('inf') for m in range(N)] for n in range(N)]
    def cost(city1, city2):
        common = abs(city2[0] - city1[0]) + abs(city2[1] - city1[1])
        z = city2[2] - city1[2]
        return common + max(0, z), common + max(0, -z)
    for n in range(N):
        for m in range(n):
            costs[n][m], costs[m][n] = cost(cities[n], cities[m])
            

    S = 2 ** N - 1
    memo = {}
    def TSP_DP_BIT(a, S, b):    # Sを集合でやると間に合わないのでbit (数字) で代用
        S = S - 2 ** a if S >> a & 1 else S
        
        if S == 0:
            memo[(a, S, b)] = costs[a][b]
            return costs[a][b]
        
        if (a, S, b) in memo:
            return memo[(a, S, b)]
        
        # S: ここに残っているパターンの情報が書かれている．
        # ここからフラグが立っているやつのパターンを全列挙したい

        # st = set()
        # for s in range(N):
        #     if S >> s & 1:
        #         st.add(costs[a][s] + TSP_DP_BIT(s, S - 2 ** s, b))
        # c_min = min(st)
        c_min = min({costs[a][s] + TSP_DP_BIT(s, S - 2 ** s, b) for s in range(N) if S >> s & 1})

        memo[(a, S, b)] = c_min
        return c_min

    print(TSP_DP_BIT(0, S, 0))
    
    # S = {n for n in range(N)}
    # memo = {}
    # def TSP_DP(a, S, b):
    #     S = S - {a}
    #     if len(S) == 0:
    #         memo[(a, tuple(S), b)] = costs[a][b]
    #         return costs[a][b]
        
    #     if (a, tuple(S), b) in memo:
    #         return memo[(a, tuple(S), b)]
        
    #     c_min = min([costs[a][s] +  TSP_DP(s, S - {s}, b) for s in S])
    #     memo[(a, tuple(S), b)] = c_min
    #     return c_min

    # print(TSP_DP(0, S, 0))
        
    

if __name__ == '__main__':
    N = int(input())
    cities = []
    for n in range(N):
        cities.append(tuple(map(int, input().split())))
    args = N, cities
    main(*args)



    