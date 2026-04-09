import heapq
import sys
from collections import defaultdict


def main() -> None:
    input = sys.stdin.readline

    H, W, N = map(int, input().split())
    hs = [0] * N
    ws = [0] * N

    by_h = defaultdict(list)  # height -> min-heap of (width, id)
    by_w = defaultdict(list)  # width -> min-heap of (height, id)

    for i in range(N):
        h, w = map(int, input().split())
        hs[i] = h
        ws[i] = w
        by_h[h].append((w, i))
        by_w[w].append((h, i))

    for h in by_h:
        heapq.heapify(by_h[h])
    for w in by_w:
        heapq.heapify(by_w[w])

    alive = [True] * N
    ans_x = [0] * N
    ans_y = [0] * N

    cur_h = H
    cur_w = W
    top = 1
    left = 1
    remain = N

    def pick_same_height() -> int:
        hp = by_h.get(cur_h)
        if hp is None:
            return -1
        while hp and not alive[hp[0][1]]:
            heapq.heappop(hp)
        if hp and hp[0][0] < cur_w:
            return hp[0][1]
        return -1

    def pick_same_width() -> int:
        hp = by_w.get(cur_w)
        if hp is None:
            return -1
        while hp and not alive[hp[0][1]]:
            heapq.heappop(hp)
        if hp and hp[0][0] < cur_h:
            return hp[0][1]
        return -1

    # Reverse simulation:
    # remove one boundary strip at a time from the current rectangle.
    for _ in range(N - 1):
        vid = pick_same_height()  # piece with h == cur_h and w < cur_w
        hid = pick_same_width()   # piece with w == cur_w and h < cur_h

        if vid == -1 and hid == -1:
            # Guaranteed input should never reach here.
            return

        if vid != -1:
            i = vid
            w = ws[i]
            # Place this strip on the right side of the current rectangle.
            ans_x[i] = top
            ans_y[i] = left + cur_w - w
            cur_w -= w
        else:
            i = hid
            h = hs[i]
            # Place this strip on the bottom side of the current rectangle.
            ans_x[i] = top + cur_h - h
            ans_y[i] = left
            cur_h -= h

        alive[i] = False
        remain -= 1

    last_id = -1
    for i in range(N):
        if alive[i]:
            last_id = i
            break

    ans_x[last_id] = top
    ans_y[last_id] = left

    out = []
    for i in range(N):
        out.append(f"{ans_x[i]} {ans_y[i]}")
    print("\n".join(out))


if __name__ == "__main__":
    main()
