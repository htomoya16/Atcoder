H, W = map(int, input().split())
S = [input() for _ in range(H)]
checked = [[False] * W for _ in range(H)]


def bfs(si, sj):
    # (si, sj) を含む白マスの領域が最外周のマスを含むか
    out = False
    q = [(si, sj)]
    checked[si][sj] = True
    for i, j in q:
        if i == 0 or i == H - 1 or j == 0 or j == W - 1:
            out = True
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ii = i + di
            jj = j + dj
            if 0 <= ii < H and 0 <= jj < W and S[ii][jj] == "." and not checked[ii][jj]:
                q.append((ii, jj))
                checked[ii][jj] = True
    return out


ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == "." and not checked[i][j]:
            if not bfs(i, j):
                ans += 1

print(ans)
