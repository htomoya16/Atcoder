import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    A = defaultdict(int)
    a = list(map(int, input().split()))
    for i in range(N):
        A[a[i]] += 1

    A_heap = list(i * -1 for i in A.keys())
    heapq.heapify(A_heap)

    for _ in range(K):
        if A_heap == []:
            break
        m = heapq.heappop(A_heap) * (-1)
        A.pop(m)
    print(A)
    ans = 0
    for k, v in A.items():
        ans += k * v
    print(ans)


if __name__ == "__main__":
    main()
