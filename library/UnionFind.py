
class UnionFind:
    def __init__(self, N):
        '''
        N: 要素の数．
        '''
        self.root = list(range(N))

    def get_root(self, x):
        '''
        x番目の根を取得．
        x: (0-index)
        '''
        if self.root[x] == x:
            return x
        else:
            self.root[x] = self.get_root(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        '''
        x番目の根とy番目の根を同じと紐づける．
        x: (0-index)
        y: (0-index)
        '''
        root_x = self.get_root(x)
        root_y = self.get_root(y)
        if root_x != root_y:
            self.root[root_x] = root_y

    def is_same(self, x, y):
        return self.get_root(x) == self.get_root(y)

    def get_groups(self):
        '''
        根をkey, 集合をvalueとしたgroupを返す．
        '''
        from collections import Counter
        return Counter(self.get_root(n) for n in range(len(self.root)))
