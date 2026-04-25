import sys

input = sys.stdin.readline


def main():
    N, Q = map(int, input().split())
    d = {k: k for k in range(1, N)}
    print(d)
    for _ in range(Q):
        C, P = map(int, input().split())
        d[C] = P
    print(d)
    ans = [0 for _ in range(N)]
    for k, v in d.items():
        ans[v] += 1

    print(*ans)


if __name__ == "__main__":
    main()
