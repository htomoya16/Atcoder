import heapq


INF = 10**18

# 使い方:
# - adj[v] = [(to, cost), ...] を作る（cost は非負）
# - dist = dijkstra(n, adj, s)
# - dist[t] が始点 s からの最短距離


def dijkstra(n, adj, s):
    """
    n: 頂点数（0..n-1）
    adj[v]: (to, cost) のリスト
    s: 始点
    return: 最短距離 dist
    """
    dist = [INF] * n
    dist[s] = 0
    hq = [(0, s)]

    while hq:
        d, v = heapq.heappop(hq)
        if d != dist[v]:
            continue
        for nv, c in adj[v]:
            nd = d + c
            if nd >= dist[nv]:
                continue
            dist[nv] = nd
            heapq.heappush(hq, (nd, nv))
    return dist
