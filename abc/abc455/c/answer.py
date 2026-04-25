import sys
from collections import Counter

input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    total = sum(A)
    removable_sums = []

    for value, count in Counter(A).items():
        removable_sums.append(value * count)

    removable_sums.sort(reverse=True)

    ans = total - sum(removable_sums[:K])
    print(ans)


if __name__ == "__main__":
    main()
