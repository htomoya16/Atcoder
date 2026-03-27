import sys

input = sys.stdin.readline


def main():
    N = int(input())
    AB = [tuple(map(int, input().split())) for _ in range(N)]

    AB.sort(key=lambda x: x[1])
    for a, b in AB:
        print(a, b)


if __name__ == "__main__":
    main()
