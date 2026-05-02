import math
import sys

input = sys.stdin.readline


def main():
    S = input().strip()

    total = 0
    for i in range(1, len(S) + 1):
        total += math.comb(len(S), i)

    print(total % 998244353)


if __name__ == "__main__":
    main()
