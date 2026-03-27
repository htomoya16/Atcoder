import sys
from collections import defaultdict

input = sys.stdin.readline


def main():
    # N = int(input())
    A = list(map(int, input().split()))

    A_dict = defaultdict(int)

    for a in A:
        A_dict[a] += 1

    A_dict_value_max = max(A_dict.values())
    for k, v in A_dict.items():
        if v == A_dict_value_max:
            print(k, v)


if __name__ == "__main__":
    main()
