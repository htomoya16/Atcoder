import sys


def main() -> None:
    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    sink = [0] * (n + 1)

    # a[i-1] >= i なので、i を大きい方から見れば sink[a[i-1]] は既に確定している。
    for i in range(n, 0, -1):
        nxt = a[i - 1]
        if nxt == i:
            sink[i] = i
        else:
            sink[i] = sink[nxt]

    print(*sink[1:])


if __name__ == "__main__":
    main()
