import sys

input = sys.stdin.readline


def main():
    X = int(input())
    if X >= 3 and X <= 18:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
