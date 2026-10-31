import bisect
import sys
input = sys.stdin.readline
H, W, N, Q = [int(x) for x in input().split()]
A, B = [], []
for n in range(N):
    r, c = [int(x) for x in input().split()]
    A.append(r)
    B.append(c)
A.sort()
B.sort()
ans = []
for q in range(Q):
    cmd, l, r = [int(x) for x in input().split()]
    if cmd == 1:
        ans.append(bisect.bisect_right(A, r) - bisect.bisect_left(A, l))
    else:
        ans.append(bisect.bisect_right(B, r) - bisect.bisect_left(B, l))
print("\n".join(map(str, ans)))
