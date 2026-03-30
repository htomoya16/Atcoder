import sys

input = sys.stdin.readline


def main():
    s = input()
    s = int(s, 2)
    print(s.bit_count())


if __name__ == "__main__":
    main()
