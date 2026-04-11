import sys
from array import array
from collections import deque


def main() -> None:
    input = sys.stdin.buffer.readline

    h, w = map(int, input().split())
    grid = []
    sx = sy = -1
    gx = gy = -1

    for i in range(h):
        row = input().strip().decode()
        grid.append(row)
        cs = row.find("S")
        if cs != -1:
            sx, sy = i, cs
        cg = row.find("G")
        if cg != -1:
            gx, gy = i, cg

    # state id: ((r * w + c) << 2) | d  (d: 0=U,1=D,2=L,3=R)
    total_states = h * w * 4
    start = total_states
    goal = total_states + 1

    # -1: unvisited, -2: root(start), otherwise previous state
    parent = array("i", [-1]) * (total_states + 2)
    parent[start] = -2

    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    q = deque([start])
    found = False

    while q:
        k = q.popleft()

        if k == start:
            # Virtual start -> states on S with arbitrary previous direction
            for sd in range(4):
                ns = ((sx * w + sy) << 2) | sd
                if parent[ns] == -1:
                    parent[ns] = start
                    q.append(ns)
            continue

        if k == goal:
            found = True
            break

        cell = k >> 2
        d1 = k & 3
        x, y = divmod(cell, w)

        if x == gx and y == gy:
            # Any direction state on G can go to virtual goal.
            if parent[goal] == -1:
                parent[goal] = k
                q.append(goal)
            continue

        ch = grid[x][y]

        for d2 in range(4):
            nx = x + dx[d2]
            ny = y + dy[d2]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if grid[nx][ny] == "#":
                continue

            allowed = False
            if d1 != d2 and ch != "o":
                allowed = True
            if d1 == d2 and ch != "x":
                allowed = True
            if not allowed:
                continue

            ns = ((nx * w + ny) << 2) | d2
            if parent[ns] == -1:
                parent[ns] = k
                q.append(ns)

    if not found:
        print("No")
        return

    ans = []
    cur = parent[goal]
    while parent[cur] != start:
        prv = parent[cur]
        x1, y1 = divmod(prv >> 2, w)
        x2, y2 = divmod(cur >> 2, w)
        if x2 == x1 - 1:
            ans.append("U")
        elif x2 == x1 + 1:
            ans.append("D")
        elif y2 == y1 - 1:
            ans.append("L")
        else:
            ans.append("R")
        cur = prv

    ans.reverse()
    print("Yes")
    print("".join(ans))


if __name__ == "__main__":
    main()
