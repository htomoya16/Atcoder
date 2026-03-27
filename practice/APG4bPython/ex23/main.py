import sys
from functools import cache

input = sys.stdin.readline


@cache
def f(n):
    if n == 0:
        return 1
    if n >= 1:
        return f(n // 2) + f(n // 3) + f(n // 5)


def main():
    N = int(input())
    print(f(N))


if __name__ == "__main__":
    main()
