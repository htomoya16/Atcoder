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

    while queue[0]:
        if queue[0]:
            t = queue.popleft()
            # if t == "G":

            # if t == ".":


if __name__ == "__main__":
    main()
