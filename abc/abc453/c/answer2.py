# bit全探索
import sys


def sgn(x: int) -> int:
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def main() -> None:
    input = sys.stdin.readline

    n = int(input())
    l = list(map(int, input().split()))
    l = [x * 2 for x in l]

    best = 0
    for mask in range(1 << n):
        pos = 1  # 0.5 * 2
        cur = 0
        for j in range(n):
            npos = pos
            if (mask >> j) & 1:
                npos += l[j]
            else:
                npos -= l[j]
            if sgn(pos) * sgn(npos) < 0:
                cur += 1
            pos = npos
        if cur > best:
            best = cur

    print(best)


if __name__ == "__main__":
    main()
