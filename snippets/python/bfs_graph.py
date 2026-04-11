from collections import deque

# 使い方:
# - 隣接リスト adj を用意して dist = bfs_graph(n, adj, s)
# - 辺重みがすべて同じ（1）な最短路で使う


def bfs_graph(n, adj, s):
    """
    n: 頂点数（0..n-1）
    adj: 隣接リスト
    s: 始点
    return: 最短距離 dist（未到達は -1）
    """
    dist = [-1] * n
    dist[s] = 0
    q = deque([s])
    while q:
        v = q.popleft()
        nd = dist[v] + 1
        for nv in adj[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = nd
            q.append(nv)
    return dist
