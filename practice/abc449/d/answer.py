import sys


def count_even(l: int, r: int) -> int:
    if l > r:
        return 0
    return r // 2 - (l - 1) // 2


def main() -> None:
    input = sys.stdin.readline
    l, r, d, u = map(int, input().split())

    even_total_y = count_even(d, u)
    max_abs_x = max(abs(l), abs(r))

    ans = 0
    for a in range(max_abs_x + 1):
        if a == 0:
            x_count = 1 if l <= 0 <= r else 0
        else:
            x_count = int(l <= a <= r) + int(l <= -a <= r)

        if x_count == 0:
            continue

        in_l = max(d, -a)
        in_r = min(u, a)
        inner_len = in_r - in_l + 1 if in_l <= in_r else 0
        inner_even = count_even(in_l, in_r) if inner_len > 0 else 0

        # |y| <= a の範囲は色が a の偶奇で決まる。外側は y の偶奇で決まる。
        black_y = even_total_y - inner_even
        if a % 2 == 0:
            black_y += inner_len

        ans += x_count * black_y

    print(ans)


if __name__ == "__main__":
    main()
