import sys
from collections import defaultdict

input = sys.stdin.readline


def main():
    N = int(input())

    A = list(map(int, input().split()))

    d = defaultdict(int)
    for s in range(N):
        if A[s] == A[A[s] - 1]:
            continue
        d[A[s]] = A[A[s] - 1]

    ans = []
    for s in range(N):
        k = A[s]
        while True:
            if not d[k]:
                ans.append(k)
                break
            else:
                k = d[k]
    print(*ans)


if __name__ == "__main__":
    main()
