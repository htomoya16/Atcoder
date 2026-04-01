import sys

input = sys.stdin.readline


def main():
    N = int(input())
    C = [[] for _ in range(N - 1)]

    for i in range(N - 1):
        for j in range(i):
            C[i].append(0)
        C[i] += list(map(int, input().split()))

    ok = False
    for a in range(N - 2):
        for b in range(a + 1, N - 1):
            for c in range(b + 1, N):
                if C[a][b - 1] + C[b - 1][c] < C[a][c]:
                    print("Yes")
                    ok = True
                    break
            if ok:
                break
        if ok:
            break
    if not ok:
        print("No")


if __name__ == "__main__":
    main()
