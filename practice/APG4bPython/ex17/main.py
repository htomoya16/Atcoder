import sys

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]

    result = [["-"] * N for _ in range(N)]

    for i in range(M):
        result[AB[i][0] - 1][AB[i][1] - 1] = "o"
        result[AB[i][1] - 1][AB[i][0] - 1] = "x"

    for i in range(N):
        print(*result[i])


if __name__ == "__main__":
    main()
