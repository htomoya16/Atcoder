import sys

input = sys.stdin.readline


def main():
    S = input().strip()

    T = []
    cnt = 0
    for i in range(len(S)):
        if S[i] == S[i - 1]:
            T.append(cnt)
            cnt = 1
            continue

        cnt += 1
    T.append(cnt)

    ans = 0
    for t in T:
        for i in range(1, t + 1):
            ans += i
    print(ans % 998244353)


if __name__ == "__main__":
    main()
