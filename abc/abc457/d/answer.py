import sys

input = sys.stdin.readline


# 計算量　log2(10^3) ≒ 10
def main():
    n, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))  # 1-indexed で扱えるようにする

    def isok(x):
        # ans を x 以上にすることができますか？
        nk = 0
        for i in range(1, n + 1):
            if a[i] < x:
                nk += (
                    (x - a[i] + i - 1) // i
                )  # ceil((x - a[i]) / i)　←ceilは小数部分があれば切り上げ。割り切れたらその数
                if nk > k:
                    return False
        return True

    # 二分探索
    ok = 1
    ng = a[1] + k + 1
    # okとngが隣り合ったら → ok = 達成できる最大値、ng = 達成できない最小値
    while ng - ok > 1:
        # 中央の値を決める
        m = (ok + ng) // 2
        if isok(m):
            # Trueなら左側
            ok = m
        else:
            # Falseなら右側
            ng = m
    print(ok)


if __name__ == "__main__":
    main()
