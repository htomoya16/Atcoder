import sys

input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())

    print(A[X - 1])


if __name__ == "__main__":
    main()
