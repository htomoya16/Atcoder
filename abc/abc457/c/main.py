import sys

input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    A = []

    for _ in range(N):
        a = list(map(int, input().split()))
        A.append(a)

    C = list(map(int, input().split()))

    for i in range(N):
        K -= C[i] * A[i][0]
        if K <= 0:
            K += C[i] * A[i][0]
            K %= A[i][0]
            if K == 0:
                K = -1
            print(A[i][K])
            break


if __name__ == "__main__":
    main()
