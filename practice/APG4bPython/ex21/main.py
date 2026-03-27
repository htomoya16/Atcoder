import sys

input = sys.stdin.readline


def main():
    A, B = map(int, input().split())
    for C in range(0, 256):
        if (A ^ C) == B:
            print(C)


if __name__ == "__main__":
    main()
