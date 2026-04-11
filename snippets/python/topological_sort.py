from collections import deque

# 使い方:
# - DAG を隣接リストで作る
# - order = topological_sort(n, adj)
# - order is None なら閉路あり


def topological_sort(n, adj):
    """
    n: 頂点数（0..n-1）
    adj: 隣接リスト
    return:
      DAGならトポロジカル順序のリスト
      閉路があるなら None
    """
    indeg = [0] * n
    for v in range(n):
        for nv in adj[v]:
            indeg[nv] += 1

    q = deque([v for v in range(n) if indeg[v] == 0])
    order = []
    while q:
        v = q.popleft()
        order.append(v)
        for nv in adj[v]:
            indeg[nv] -= 1
            if indeg[nv] == 0:
                q.append(nv)

    if len(order) != n:
        return None
    return order
