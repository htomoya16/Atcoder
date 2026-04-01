N = int(input())
C = [[None] * (i + 1) + list(map(int, input().split())) for i in range(N - 1)]
ans = "No"
for a in range(N):
    for b in range(a + 1, N):
        for c in range(b + 1, N):
            if C[a][b] + C[b][c] < C[a][c]:
                ans = "Yes"
print(ans)
