class SegTree:
    """
    反復（非再帰）セグメント木
    例:
        op = min, e = 10**18
        op = max, e = -10**18
        op = lambda a,b: a+b, e = 0
    """
    # 使い方:
    # - st = SegTree(n, op, e)
    # - st.build(arr) で初期化
    # - st.set(i, x) で一点更新
    # - st.prod(l, r) で区間 [l, r) 取得

    def __init__(self, n, op, e):
        self.op = op
        self.e = e
        self.size = 1
        while self.size < n:
            self.size <<= 1
        self.data = [e] * (2 * self.size)

    def build(self, arr):
        for i, v in enumerate(arr):
            self.data[self.size + i] = v
        for i in range(self.size - 1, 0, -1):
            self.data[i] = self.op(self.data[i << 1], self.data[i << 1 | 1])

    def set(self, i, x):
        i += self.size
        self.data[i] = x
        i >>= 1
        while i:
            self.data[i] = self.op(self.data[i << 1], self.data[i << 1 | 1])
            i >>= 1

    def get(self, i):
        return self.data[self.size + i]

    def prod(self, l, r):
        """
        区間 [l, r) の畳み込み結果を返す
        """
        sml = self.e
        smr = self.e
        l += self.size
        r += self.size
        while l < r:
            if l & 1:
                sml = self.op(sml, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.data[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)
