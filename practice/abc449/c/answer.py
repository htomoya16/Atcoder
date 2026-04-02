import sys


def main() -> None:
    input = sys.stdin.readline
    n, l, r = map(int, input().split())
    s = input().strip()

    # freq[x] = 現在の j に対して、距離条件を満たす i のうち文字 x の個数
    freq = [0] * 26
    ans = 0

    for j in range(n):
        add_idx = j - l
        if add_idx >= 0:
            freq[ord(s[add_idx]) - 97] += 1

        remove_idx = j - r - 1
        if remove_idx >= 0:
            freq[ord(s[remove_idx]) - 97] -= 1

        ans += freq[ord(s[j]) - 97]

    print(ans)


if __name__ == "__main__":
    main()
