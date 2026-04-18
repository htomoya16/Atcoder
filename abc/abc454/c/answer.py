import sys
from collections import deque

input = sys.stdin.readline


# snippets/python/bfs_graph.py
def bfs_graph(n, adj, s):
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


def main() -> None:
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)

    dist = bfs_graph(n, graph, 0)
    # dist[i] は「アイテム1から 頂点i(アイテム) へ到達する最小交換回数」。
    # -1 でなければそのアイテムは入手可能。
    # 到達可能なアイテムの種類数を数える
    print(sum(d != -1 for d in dist))


if __name__ == "__main__":
    main()
