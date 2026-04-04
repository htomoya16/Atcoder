import sys


def decompose(s: str):
    core = []
    gaps = []
    cnt_a = 0
    for ch in s:
        if ch == "A":
            cnt_a += 1
        else:
            gaps.append(cnt_a)
            core.append(ch)
            cnt_a = 0
    gaps.append(cnt_a)
    return core, gaps


def main() -> None:
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()

    core_s, gaps_s = decompose(s)
    core_t, gaps_t = decompose(t)

    # A 以外の相対順序が一致しないと変換不可能
    if core_s != core_t:
        print(-1)
        return

    # 各ギャップの A 個数を一致させる最小操作回数 = L1 距離
    ans = 0
    for x, y in zip(gaps_s, gaps_t):
        ans += abs(x - y)

    print(ans)


if __name__ == "__main__":
    main()
