import sys

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    F = list(map(int, input().split()))

    d = {i + 1: 0 for i in range(M)}
    for f in F:
        d[f] += 1

    ok1 = True
    ok2 = True
    for k, v in d.items():
        if v == 0:
            ok2 = False
        if v > 1:
            ok1 = False

    print("Yes" if ok1 else "No")
    print("Yes" if ok2 else "No")


if __name__ == "__main__":
    main()
