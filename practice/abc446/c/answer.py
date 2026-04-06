import sys
from collections import deque


def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    t = next(it)
    out = []

    for _ in range(t):
        n = next(it)
        d = next(it)
        a = [next(it) for _ in range(n)]
        b = [next(it) for _ in range(n)]

        q = deque()  # (purchase_day, remaining_count)
        total = 0

        for day in range(1, n + 1):
            add_cnt = a[day - 1]
            q.append((day, add_cnt))
            total += add_cnt

            use = b[day - 1]
            while use > 0:
                buy_day, cnt = q[0]
                take = min(use, cnt)
                cnt -= take
                use -= take
                total -= take
                if cnt == 0:
                    q.popleft()
                else:
                    q[0] = (buy_day, cnt)

            expire_day = day - d
            while q and q[0][0] <= expire_day:
                _, cnt = q.popleft()
                total -= cnt

        out.append(str(total))

    sys.stdout.write("\n".join(out))
    print("")


if __name__ == "__main__":
    solve()
