import sys
from collections import defaultdict

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    teamA = defaultdict(int)
    teamB = defaultdict(int)

    for i in range(N):
        A, B = map(int, input().split())
        teamA[A] += 1
        teamB[B] += 1

    for j in range(1, M + 1):
        print(teamB[j] - teamA[j])


if __name__ == "__main__":
    main()
