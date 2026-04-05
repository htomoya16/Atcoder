import sys


def main() -> None:
    input = sys.stdin.buffer.readline

    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        ai, bi = map(int, input().split())
        a[i] = ai
        b[i] = bi

    m = int(input())
    s_list = [input().strip().decode() for _ in range(m)]

    # exists[len][pos][ch] = その条件を満たす文字列が1つ以上あるか
    exists = [[[False] * 26 for _ in range(11)] for _ in range(11)]
    for s in s_list:
        length = len(s)
        for pos, ch in enumerate(s, start=1):
            exists[length][pos][ord(ch) - 97] = True

    out = []
    for s in s_list:
        if len(s) != n:
            out.append("No")
            continue

        ok = True
        for i in range(n):
            ch_idx = ord(s[i]) - 97
            if not exists[a[i]][b[i]][ch_idx]:
                ok = False
                break

        out.append("Yes" if ok else "No")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
