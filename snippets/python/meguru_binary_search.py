def meguru_bisect(ok, ng, is_ok):
    """
    めぐる式二分探索
    前提:
      - is_ok(ok) == True
      - is_ok(ng) == False
      - 単調条件で ok と ng が分かれている
    戻り値:
      境界側の ok
    """
    # 使い方:
    # - 判定関数 is_ok(mid) を作る（単調性が必要）
    # - ok に「条件を満たす値」、ng に「満たさない値」を置く
    # - ans = meguru_bisect(ok, ng, is_ok)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok
