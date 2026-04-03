import sys


def main() -> None:
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

    # freq[val] = 現在の root(=1) からのパスで val が何回出るか
    freq = {}
    dup_kind = 0  # 出現回数が2以上の値の種類数
    ans = [False] * n

    # stack: (node, parent, phase)
    # phase=0: 入る処理, phase=1: 出る処理
    stack = [(0, -1, 0)]

    while stack:
        node, parent, phase = stack.pop()

        if phase == 0:
            val = a[node]
            c = freq.get(val, 0)
            if c == 1:
                dup_kind += 1
            freq[val] = c + 1

            ans[node] = dup_kind > 0

            stack.append((node, parent, 1))
            for nxt in graph[node]:
                if nxt == parent:
                    continue
                stack.append((nxt, node, 0))
        else:
            val = a[node]
            c = freq[val]
            if c == 2:
                dup_kind -= 1
            if c == 1:
                del freq[val]
            else:
                freq[val] = c - 1

    out = ["Yes" if x else "No" for x in ans]
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
