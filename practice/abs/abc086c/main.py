import sys

input = sys.stdin.readline


def main():
    N = int(input())
    for i in range(N):
        T, X, Y = map(int, input().split())

    dp = [[] for _ in range(N)]
    dp[0] = [0, 0]

    for t in range(N):
        print(dp[t][0])
        if dp[t][0] + 1 < N:
            dp[t + 1].append([dp[t][0] + 1, dp[t][1]])
        if dp[t][1] + 1 < N:
            dp[t + 1].append([dp[t][0], dp[t][1] + 1])
        if dp[t][0] - 1 > 0:
            dp[t + 1].append([dp[t][0] - 1, dp[t][1]])
        if dp[t][0] - 1 > N:
            dp[t + 1].append([dp[t][0], dp[t][1] - 1])

    for i in range(N):
        if dp[T[i]] == []:
            print("No")
            break
    else:
        print("Yes")


if __name__ == "__main__":
    main()
