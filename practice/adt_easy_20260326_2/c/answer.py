import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    a = data[2:2 + m]

    # connected[i] = True のとき、i と i+1 は同じ連結成分
    connected = [False] * (n + 1)
    for x in a:
        connected[x] = True

    ans = []
    i = 1
    while i <= n:
        j = i
        while j <= n - 1 and connected[j]:
            j += 1

        # 連結成分 [i, j] を大きい順に読む
        for v in range(j, i - 1, -1):
            ans.append(v)

        i = j + 1

    print(*ans)


if __name__ == "__main__":
    main()
