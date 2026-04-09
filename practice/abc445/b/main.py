import sys

input = sys.stdin.readline


def main():
    N = int(input())
    S = [input().strip() for _ in range(N)]

    m = max(len(s) for s in S)

    for s in S:
        diff = (m - len(s)) // 2
        print("." * diff + s + "." * diff)


if __name__ == "__main__":
    main()
