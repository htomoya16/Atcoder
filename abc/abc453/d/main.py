import sys
from collections import deque

input = sys.stdin.readline


def main():
    H, W = map(int, input().split())
    S = [[[] for _ in range(W)] for _ in range(H)]

    queue = deque()
    for i in range(H):
        s = input().strip()
        for j in range(W):
            S[i][j] = s[j]
            if s[j] == "S":
                queue.append(S[i][j])

    active = [[[False] for _ in range(W)] for _ in range(H)]

    def dfs(i, j):
        if active[i][j]:
            return
        if S[i][j] == "#":
            return

        active[i][j] = True

        if S[i][j] == "G":
            return []

        if S[i][j] == ".":
            l = dfs(i + 1, j)
            # if type(l) == type("list"):
            #    return l.append("R")

    while queue[0]:
        if queue[0]:
            t = queue.popleft()
            # if t == "G":

            # if t == ".":


if __name__ == "__main__":
    main()
