import sys

input = sys.stdin.readline


def main():
    N, L, R = map(int, input().split())
    S = input()

    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            if not (L <= j - i and j - i <= R):
                continue

            if S[i] == S[j]:
                cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
