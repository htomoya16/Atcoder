from collections import deque

# 使い方:
# - grid と開始点 starts を渡す
# - 返り値 dist[r][c] は最短距離（未到達は -1）
# - 典型: dist = bfs_grid(grid, [(sr, sc)])


def bfs_grid(grid, starts):
    """
    grid: 盤面（list[str]）
    starts: 開始地点の列挙（(r, c)）
    return: 最短距離 dist[h][w]（未到達は -1）
    """
    h = len(grid)
    w = len(grid[0])
    dist = [[-1] * w for _ in range(h)]
    q = deque()

    for r, c in starts:
        if 0 <= r < h and 0 <= c < w and grid[r][c] != "#":
            if dist[r][c] == -1:
                dist[r][c] = 0
                q.append((r, c))

    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    while q:
        r, c = q.popleft()
        nd = dist[r][c] + 1
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr < 0 or nr >= h or nc < 0 or nc >= w:
                continue
            if grid[nr][nc] == "#" or dist[nr][nc] != -1:
                continue
            dist[nr][nc] = nd
            q.append((nr, nc))
    return dist
