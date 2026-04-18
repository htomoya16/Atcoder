import sys

input = sys.stdin.readline


def main():
    L, R = map(int, input().split())
    print(R - L + 1)


if __name__ == "__main__":
    main()
