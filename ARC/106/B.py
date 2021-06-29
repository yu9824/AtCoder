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



class UnionFind:
    def __init__(self, N):
        self.root = [n for n in range(N)]

    def get_root(self, x):
        if self.root[x] == x:
            return x
        else:
            self.root[x] = self.get_root(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        root_x = self.get_root(x)
        root_y = self.get_root(y)
        if root_x != root_y:
            self.root[root_x] = root_y

def main(*args):
    N, M, A, B, CD = args
    uf = UnionFind(N)

    for c, d in CD:
        uf.unite(c-1, d-1)
    groups = {}
    for n in range(N):
        r = uf.get_root(n)  # 完璧な根っこを取得
        if r in groups:
            groups[r].add(n)
        else:
            groups[r] = {n}

    for v in groups.values():
        sum_a = 0
        sum_b = 0
        for i in v:
            sum_a += A[i]
            sum_b += B[i]
        if sum_a != sum_b:
            print('No')
            break
    else:
        print('Yes')

N, M = tuple(map(int, input().split()))
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
CD = set()
for m in range(M):
    CD.add(tuple(map(int, input().split())))
main(N, M, A, B, CD)

    