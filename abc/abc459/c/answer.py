import sys

input = sys.stdin.readline


def main():
    n, q = map(int, input().split())

    stacked = [0] * (n + 1)
    count = [0] * (q + 2)
    removed = 0
    ans = []

    for _ in range(q):
        t, x = map(int, input().split())

        if t == 1:
            stacked[x] += 1
            count[stacked[x]] += 1

            if count[stacked[x]] == n:
                removed = stacked[x]
        else:
            border = x + removed

            if border > q:
                ans.append("0")
            else:
                ans.append(str(count[border]))

    print("\n".join(ans))


if __name__ == "__main__":
    main()
