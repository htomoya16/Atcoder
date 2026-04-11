import sys


def main() -> None:
    input = sys.stdin.readline

    n = int(input())
    l = list(map(int, input().split()))

    # 座標を2倍して整数で扱う:
    # 開始位置 0.5 -> 1, 各移動長 Li -> 2*Li
    dp = {1: 0}  # position -> max crossings

    for x in l:
        step = 2 * x
        ndp = {}
        for pos, score in dp.items():
            for nxt in (pos + step, pos - step):
                add = 1 if pos * nxt < 0 else 0
                best = score + add
                if nxt not in ndp or ndp[nxt] < best:
                    ndp[nxt] = best
        dp = ndp

    print(max(dp.values()))


if __name__ == "__main__":
    main()
