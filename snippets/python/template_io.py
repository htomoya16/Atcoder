import sys

input = sys.stdin.readline

# 使い方:
# - 問題ファイルへこの入出力ヘルパーを貼る
# - ii / mi / li を必要な分だけ呼ぶ
# - main() に処理本体を書く


def ii() -> int:
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(map(int, input().split()))


def main() -> None:
    # 例:
    # n = ii()
    # a = li()
    pass


if __name__ == "__main__":
    main()
