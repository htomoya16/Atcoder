from collections import deque

# 使い方:
# - 隣接リスト adj を用意して dist = bfs_graph(n, adj, s)
# - 辺重みがすべて同じ（1）な最短路で使う


def bfs_graph(n, adj, s):
    """
    n: 頂点数（0..n-1）
    adj: 隣接リスト
    s: 始点
    return: dist (dist[i] 頂点 s から頂点 i まで、辺を何本通れば行けるか（未到達は -1）)

    flow:
    1. dist を -1 で初期化し、始点 s だけ dist[s] = 0 にする
    2. キューに始点を入れる
    3. キューから頂点 v を取り出し、隣接頂点 nv を順に見る
    4. dist[nv] == -1（未到達）なら dist[nv] = dist[v] + 1 (距離を1増やす)にしてキューへ追加
    5. キューが空になるまで繰り返し、dist を返す
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
