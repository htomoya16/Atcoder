import sys

input = sys.stdin.readline


def main():
    s = input()

    if (len(s) - 1) % 5 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
