class UnionFind(object):
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def isConnected(self, u, v):
        return self.find(u) == self.find(v)

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False

        if self.rank[pv] > self.rank[pu]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pu] = pv
            self.rank[pv] += 1
        return True

u = UnionFind(6)

u.union(3, 4)
u.union(2, 3)
u.union(1, 2)
u.union(0, 1)