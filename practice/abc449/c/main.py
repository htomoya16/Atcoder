import sys

input = sys.stdin.readline


def main():
    N, L, R = map(int, input().split())
    S = input()

    cnt = 0
    for i in range(N):
        cnt += S.count(S[i], i + L, i + R + 1)
    print(cnt)


if __name__ == "__main__":
    main()
