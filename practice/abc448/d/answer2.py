import sys


def main() -> None:
    sys.setrecursionlimit(1_000_000)
    data = list(map(int, sys.stdin.buffer.read().split()))
    ptr = 0

    n = data[ptr]
    ptr += 1
    a = data[ptr : ptr + n]
    ptr += n

    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u = data[ptr] - 1
        v = data[ptr + 1] - 1
        ptr += 2
        graph[u].append(v)
        graph[v].append(u)

    freq = {}
    dup_kind = 0
    ans = [False] * n

    def dfs(v: int, pv: int) -> None:
        nonlocal dup_kind

        val = a[v]
        c = freq.get(val, 0)
        if c == 1:
            dup_kind += 1
        freq[val] = c + 1

        ans[v] = dup_kind > 0

        for nx in graph[v]:
            if nx == pv:
                continue
            dfs(nx, v)

        c = freq[val]
        if c == 2:
            dup_kind -= 1
        if c == 1:
            del freq[val]
        else:
            freq[val] = c - 1

    dfs(0, -1)

    out = ["Yes" if x else "No" for x in ans]
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
