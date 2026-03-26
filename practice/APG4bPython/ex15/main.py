import sys

input = sys.stdin.readline


def main():
    N, S = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # リンゴ・パイナップルをそれぞれ1つずつ購入するとき合計S円になるような買い方が何通りあるか
    # ここにプログラムを追記
    ans = 0
    for a in A:
        for b in B:
            if a + b == S:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
