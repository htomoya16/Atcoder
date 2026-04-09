import sys


def main() -> None:
    input = sys.stdin.readline

    H, W, N = map(int, input().split())
    h = [0] * N
    w = [0] * N
    for i in range(N):
        h[i], w[i] = map(int, input().split())

    # ord_h: h が大きい順, ord_w: w が大きい順
    ord_h = list(range(N))
    ord_h.sort(key=lambda i: h[i], reverse=True)
    ord_w = list(range(N))
    ord_w.sort(key=lambda i: w[i], reverse=True)

    ans_x = [-1] * N
    ans_y = [-1] * N
    used = [False] * N

    ith = 0
    itw = 0

    for _ in range(N):
        while used[ord_h[ith]]:
            ith += 1
        while used[ord_w[itw]]:
            itw += 1

        # C++ 実装と同様:
        # 最大高さ側が現在高さ H に一致すればそれを使い、そうでなければ最大幅側を使う。
        if h[ord_h[ith]] == H:
            i = ord_h[ith]
        else:
            i = ord_w[itw]

        # 右下に配置（1-indexed）
        ans_x[i] = H - h[i] + 1
        ans_y[i] = W - w[i] + 1
        used[i] = True

        if h[i] == H:
            W -= w[i]
        else:
            H -= h[i]

    out = []
    for i in range(N):
        out.append(f"{ans_x[i]} {ans_y[i]}")
    print("\n".join(out))


if __name__ == "__main__":
    main()
