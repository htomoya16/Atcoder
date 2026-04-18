import sys

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())

    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

    used = [False for _ in range(N)]
    depth = [0 for _ in range(N)]

    def dfs(cur):

        if not graph[cur]:
            return depth

        for e in graph[cur]:
            if not used[e]:
                used[e] = True
                depth[e] += 1

                return dfs(e)

    dfs(0)
    print(max(depth))


if __name__ == "__main__":
    main()
