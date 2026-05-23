import sys

input = sys.stdin.readline


def main():
    s = "HelloWorld"
    index = int(input())
    s = s[: index - 1] + s[index:]
    print(s)


if __name__ == "__main__":
    main()
