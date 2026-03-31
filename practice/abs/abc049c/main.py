import sys

input = sys.stdin.readline


def f(s):
    array = ["dream", "dreamer", "erase", "eraser"]

    for v in array:
        if len(s) < len(v):
            return False
        if s[: len(v)] == v:
            if len(s) == len(v):
                return True
            else:
                return f(s[len(v) :])


def main():
    s = input().replace("\n", "")
    if f(s):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
