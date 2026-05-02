from collections import defaultdict

S = input()
dp = defaultdict(int)
for c in S:
    dp[c] = (dp["a"] + dp["b"] + dp["c"] + 1) % 998244353
print(sum(dp.values()) % 998244353)
