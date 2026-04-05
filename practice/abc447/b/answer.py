s = input()
cnt = {c: s.count(c) for c in s}
ma = max(cnt.values())
print("".join(c for c in s if cnt[c] != ma))
