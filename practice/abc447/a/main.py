import sys

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())

    if N % 2 == 1:
        N += 1

    if N // 2 >= M:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
