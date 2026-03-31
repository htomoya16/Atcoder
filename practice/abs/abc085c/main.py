import sys

input = sys.stdin.readline


def main():
    N, Y = map(int, input().split())

    ok = False

    for x in range(N + 1):
        for y in range(N - x + 1):
            z = N - x - y
            if 10000 * x + 5000 * y + 1000 * z == Y:
                print(x, y, z)
                ok = True
        if ok:
            break
    else:
        print(-1, -1, -1)


if __name__ == "__main__":
    main()
