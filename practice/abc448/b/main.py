import sys

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    C = [None] + list(map(int, input().split()))

    used = [None] + [0] * M

    for i in range(N):
        A, B = map(int, input().split())
        used[A] += B
    ans = 0
    for i in range(1, M + 1):
        if used[i] > C[i]:
            ans += C[i]
        else:
            ans += used[i]
    print(ans)


if __name__ == "__main__":
    main()
