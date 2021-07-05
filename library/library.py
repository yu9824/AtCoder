


def cmb(n,r):
    from operator import mul
    from functools import reduce

    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

def argsort(seq, reverse = False):
    # http://stackoverflow.com/questions/3071415/efficient-method-to-calculate-the-rank-vector-of-a-list-in-python
    # https://stackoverflow.com/questions/3382352/equivalent-of-numpy-argsort-in-basic-python
    return sorted(range(len(seq)), key=seq.__getitem__, reverse = reverse)

class Node:
    def __init__(self, node_id):
        self.parent = -1
        self.children = []
        self.depth = 0
        self.node_id = node_id
        self.c = 0

    def update(self, parent_node):
        self.depth = parent_node.depth + 1
        parent_node.children.append(self.node_id)
        self.parent = parent_node.node_id

