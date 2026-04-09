import sys
from collections import defaultdict

input = sys.stdin.readline


def main():
    N = int(input())

    A = list(map(int, input().split()))

    ans = []
    dp = defaultdict(int)
    for s in range(N):
        k = A[s]
        if dp[k]:
            ans.append(dp[k])
        else:
            tmp = defaultdict(int)
            while k != A[k - 1]:
                tmp[k] = 0
                k = A[k - 1]
            ans.append(k)
            for key in tmp.keys():
                tmp[key] = k

            dp.update(tmp)
    print(*ans)


if __name__ == "__main__":
    main()
