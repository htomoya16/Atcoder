import sys

input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    S = [i for i in input().split()]

    ans = [i for i in S if len(i) >= K]

    print(*ans)


if __name__ == "__main__":
    main()
