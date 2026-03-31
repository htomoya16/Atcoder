import sys

input = sys.stdin.readline


def main() -> None:
    n = int(input())

    prev_t, prev_x, prev_y = 0, 0, 0

    for _ in range(n):
        t, x, y = map(int, input().split())

        dt = t - prev_t
        dist = abs(x - prev_x) + abs(y - prev_y)

        if dist > dt or (dt - dist) % 2 == 1:
            print("No")
            return

        prev_t, prev_x, prev_y = t, x, y

    print("Yes")


if __name__ == "__main__":
    main()
