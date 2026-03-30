import sys

input = sys.stdin.readline


def main():
    a, b = map(int, input().split())
    c = a * b
    if c % 2 == 0:
        print("Even")
    elif c % 2 == 1:
        print("Odd")


if __name__ == "__main__":
    main()
