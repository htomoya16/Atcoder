import sys

input = sys.stdin.readline


def main():
    N = int(input())
    A = []

    for _ in range(N):
        a = list(map(int, input().split()))
        A.append(a)

    X, Y = map(int, input().split())
    print(A[X - 1][Y])


if __name__ == "__main__":
    main()
