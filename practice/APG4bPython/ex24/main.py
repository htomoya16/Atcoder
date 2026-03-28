import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def popcount(n):
    return n.bit_count()


def f(n):
    if n == 0:
        return 0
    if n >= 0 and popcount(n) % 2 == 1:
        return f(n - 1) + 1
    if n >= 0 and popcount(n) % 2 == 0:
        return f(n - 2) + 1


def main():
    n = int(input())
    print(f(n))


if __name__ == "__main__":
    main()
