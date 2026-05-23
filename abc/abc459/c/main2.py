import sys

input = sys.stdin.readline


def main():
    n, q = map(int, input().split())

    block = [0 for _ in range(n)]
    block_num = [n] + [0 for _ in range(n)]

    flag_num = 0

    k = 0

    for _ in range(q):
        t, x = map(int, input().split())

        if t == 1:
            if block[x] == k:
                flag_num += 1
            block[x] += 1
            if flag_num == n:
                k += 1
            block_num[block[q]] += 1
        else:
            ans = 0
            for i in range(x + 1, n + 1):
                ans += block_num[i - k]
            print(ans)


if __name__ == "__main__":
    main()
