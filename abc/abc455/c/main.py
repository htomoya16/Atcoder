import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline


def main():
    N, K = map(int, input().split())

    A = defaultdict(int)
    A_sum = defaultdict(int)
    a = list(map(int, input().split()))
    for i in range(N):
        A[a[i]] += 1

    A_heap = list(i * -1 for i in A.keys())
    heapq.heapify(A_heap)

    ans = 0
    for k, v in A.items():
        A_sum[k] = k * v
        ans += k * v

    A_sum_s = sorted(A_sum.items(), key=lambda x: x[1])

    for i in range(K):
        if A_sum_s == []:
            break
        k = A_sum_s.pop(-1)
        ans -= k[1]
    print(ans)


if __name__ == "__main__":
    main()
