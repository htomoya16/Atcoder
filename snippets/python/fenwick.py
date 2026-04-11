class Fenwick:
    """
    1-indexed Binary Indexed Tree（Fenwick Tree）
    """
    # 使い方:
    # - fw = Fenwick(n)
    # - fw.add(i, x) で i 番目（1-indexed）へ加算
    # - fw.sum_prefix(i) で [1, i] の和
    # - fw.sum_range(l, r) で [l, r] の和

    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & -i

    def sum_prefix(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def sum_range(self, l, r):
        return self.sum_prefix(r) - self.sum_prefix(l - 1)
