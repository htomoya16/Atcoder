import sys


def main() -> None:
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()

    n = len(s)
    m = len(t)

    # best[k] = 先頭から現在位置までで、Tの先頭k文字を部分列として作れるときの
    #           "開始位置" の最大値（作れなければ -1）
    best = [-1] * (m + 1)

    contains = 0
    for i, ch in enumerate(s):
        # 同じ文字を同一ステップで二重利用しないため逆順更新
        for k in range(m, 0, -1):
            if ch != t[k - 1]:
                continue
            if k == 1:
                if i > best[1]:
                    best[1] = i
            else:
                prev = best[k - 1]
                if prev != -1 and prev > best[k]:
                    best[k] = prev

        # 末尾が i の部分文字列で T を部分列に含む個数
        if best[m] != -1:
            contains += best[m] + 1

    total = n * (n + 1) // 2
    print(total - contains)


if __name__ == "__main__":
    main()
