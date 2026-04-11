class ModComb:
    """mod 上の組み合わせ nCk を高速に計算するための前計算クラス"""
    # 使い方:
    # - mc = ModComb(n_max, mod)
    # - mc.nCk(n, k) で nCk (mod mod)

    def __init__(self, n_max, mod):
        self.mod = mod
        self.fact = [1] * (n_max + 1)
        self.ifact = [1] * (n_max + 1)
        for i in range(1, n_max + 1):
            self.fact[i] = self.fact[i - 1] * i % mod
        self.ifact[n_max] = pow(self.fact[n_max], mod - 2, mod)
        for i in range(n_max, 0, -1):
            self.ifact[i - 1] = self.ifact[i] * i % mod

    def nCk(self, n, k):
        if k < 0 or k > n:
            return 0
        return self.fact[n] * self.ifact[k] % self.mod * self.ifact[n - k] % self.mod
