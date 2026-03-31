import sys

input = sys.stdin.readline


def main() -> None:
    s = input().strip()
    words = ["dream", "dreamer", "erase", "eraser"]

    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(n + 1):
        if not dp[i]:
            continue
        for w in words:
            j = i + len(w)
            if j <= n and s[i:j] == w:
                dp[j] = True

    print("YES" if dp[n] else "NO")


if __name__ == "__main__":
    main()
