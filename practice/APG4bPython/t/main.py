import sys

input = sys.stdin.readline


def main():
    N = int(input())

    # p[i] : 組織 i の親組織
    p = [-1] + list(map(int, input().split()))

    # 2 次元配列 children
    # children[i] : 組織 i の子組織の一覧 であるような 2 次元配列
    children = [[] for _ in range(N)]
    for i in range(1, N):
        children[p[i]].append(i)

    # 再帰関数 complete_time
    # 入力 : 組織番号 x
    # 出力 : 組織 x に子組織からの報告書が揃った時刻（報告書を親組織へ送った時刻）
    def complete_time(x):
        # ベースケース : 子組織が存在しない場合、答えは 0
        if len(children[x]) == 0:
            return 0

        # 子組織が存在する場合、答えは「子組織から報告書が届く時刻」の最大値
        return max(complete_time(y) + 1 for y in children[x])

    # 組織 0 の元に報告書が揃う時刻を出力
    print(complete_time(0))


if __name__ == "__main__":
    main()
