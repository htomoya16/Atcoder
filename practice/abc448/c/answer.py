import sys


def main() -> None:
    input = sys.stdin.readline
    n, q = map(int, input().split())
    vals = list(map(int, input().split()))
    a = [(vals[i], i + 1) for i in range(n)]
    a.sort()

    out = []
    for _ in range(q):
        k = int(input())
        b = list(map(int, input().split()))

        i = 0
        while True:
            if a[i][1] in b:
                i += 1
                continue
            out.append(str(a[i][0]))
            break

    print("\n".join(out))


if __name__ == "__main__":
    main()
