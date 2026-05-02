import sys

input = sys.stdin.readline


def main():
    A = [[] for _ in range(3)]
    for i in range(3):
        A[i] = list(map(int, input().split()))

    cnt = 0
    tmp = set()
    for i in range(6):
        if 4 <= A[0][i] and A[0][i] <= 6 and A[0][i] not in tmp:
            tmp.add(A[0][i])
            for j in range(6):
                if 4 <= A[1][j] and A[1][j] <= 6 and A[1][j] not in tmp:
                    tmp.add(A[1][j])
                    for k in range(6):
                        if 4 <= A[2][k] and A[2][k] <= 6 and A[2][k] not in tmp:
                            tmp.add(A[2][k])
                            cnt += 1
                            tmp.remove(A[2][k])
                    tmp.remove(A[1][j])
            tmp.remove(A[0][i])

    print(cnt / (6 * 6 * 6))


if __name__ == "__main__":
    main()
