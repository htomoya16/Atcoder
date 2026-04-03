import sys

input = sys.stdin.readline


def main():
    N, Q = map(int, input().split())
    key = [i for i in range(N)]
    values = list(map(int, input().split()))
    A = dict(zip(key, values))
    B = dict(sorted(A.items(), key=lambda x: x[1]))

    print(B)


if __name__ == "__main__":
    main()
