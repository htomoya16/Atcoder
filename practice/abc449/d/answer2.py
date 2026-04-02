import sys


def main() -> None:
    input = sys.stdin.readline
    l, r, d, u = map(int, input().split())

    ans = 0

    # |x| > |y| の領域
    for x in range(l, r + 1):
        if x % 2 != 0:
            continue
        low = max(d, -abs(x) + 1)
        high = min(u, abs(x) - 1)
        cnt = high - low + 1
        if cnt > 0:
            ans += cnt

    # |x| <= |y| の領域
    for y in range(d, u + 1):
        if y % 2 != 0:
            continue
        left = max(l, -abs(y))
        right = min(r, abs(y))
        cnt = right - left + 1
        if cnt > 0:
            ans += cnt

    print(ans)


if __name__ == "__main__":
    main()
