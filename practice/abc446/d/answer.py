from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
d = defaultdict(int)
for v in a:
    d[v] = max(d[v], d[v - 1] + 1)
print(max(d.values()))
