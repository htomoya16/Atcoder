class UnionFind:
    """Union-Find（Disjoint Set Union）"""
    # 使い方:
    # - uf = UnionFind(n)
    # - uf.merge(a, b) で連結
    # - uf.same(a, b) で同一連結成分か判定
    # - uf.size(a) で成分サイズ取得

    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.size_arr = [1] * n

    def leader(self, a):
        p = self.parent[a]
        if p == a:
            return a
        self.parent[a] = self.leader(p)
        return self.parent[a]

    def same(self, a, b):
        return self.leader(a) == self.leader(b)

    def merge(self, a, b):
        x = self.leader(a)
        y = self.leader(b)
        if x == y:
            return x
        if self.size_arr[x] < self.size_arr[y]:
            x, y = y, x
        self.parent[y] = x
        self.size_arr[x] += self.size_arr[y]
        return x

    def size(self, a):
        return self.size_arr[self.leader(a)]
