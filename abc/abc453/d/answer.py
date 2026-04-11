import sys
from array import array


def main() -> None:
    input = sys.stdin.buffer.readline

    # ------------------------------------------------------------
    # 1) 入力を読み、S / G の位置を探す
    # ------------------------------------------------------------
    h, w = map(int, input().split())
    grid = []
    s_idx = -1
    g_idx = -1

    for r in range(h):
        row = input().strip().decode()
        grid.append(row)
        cs = row.find("S")
        if cs != -1:
            s_idx = r * w + cs
        cg = row.find("G")
        if cg != -1:
            g_idx = r * w + cg

    # ------------------------------------------------------------
    # 2) 状態空間の定義
    #    state = (マス番号, 直前の移動方向)
    #    方向ID: 0=U, 1=D, 2=L, 3=R
    #
    # 直前方向が必要な理由:
    #   - 'o' マス: 同じ方向に進む必要がある
    #   - 'x' マス: 方向を変える必要がある
    #
    # エンコード:
    #   state_id = cell_index * 4 + dir
    #   cell_index = state_id >> 2
    #   dir = state_id & 0b11
    #   ※ 方向は4通りなので2bitで表せる。
    #      cell_index を2bit左にずらして下位2bitに dir を入れる。
    #
    # (cell, dir) を1つの整数 ns にまとめる理由:
    #   - parent / move_dir を「整数添字の配列」で持てるので高速
    #   - tuple を大量に持たずに済み、メモリを抑えられる
    #   - キューにも整数1個だけを入れればよく実装がシンプル
    # ------------------------------------------------------------
    n_cells = h * w
    n_states = n_cells * 4

    # parent[state]:
    #   その状態に「どの状態から来たか」を記録する配列。
    #   これがあると、goal に着いたあとに逆向きにたどって
    #   実際の移動経路を復元できる。
    #   値の意味:
    #     -2 : 未訪問
    #     -1 : 仮想開始点から直接到達（S からの1手目）
    #     >=0: 1つ前の状態ID
    #
    # メモリ削減のため list[int] ではなく array('i') を使う。
    parent = array("i", [-2]) * n_states
    # move_dir[state]:
    #   その状態に「入るときに使った方向」を保存する配列。
    #   parent だけでも経路復元はできるが、方向文字(UDLR)を
    #   直接出したいので持っておく。
    #   方向は4種類(0..3)なので bytearray で十分。
    move_dir = bytearray(n_states)

    # U, D, L, R の方向ベクトル
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    dir_char = "UDLR"

    # BFSキュー:
    #   「これから探索する状態」を入れる。
    #   head 添字を進める方式にすると先頭取り出しが O(1)。
    #   （pop(0) のような O(n) を避ける）
    q = array("I")

    sr, sc = divmod(s_idx, w)
    # ------------------------------------------------------------
    # 3) BFS初期化
    #    S では直前方向がないので最初の1手は自由。
    #    行ける隣接マスを方向付き状態としてキューに入れる。
    # ------------------------------------------------------------
    for d in range(4):
        nr = sr + dr[d]
        nc = sc + dc[d]
        if nr < 0 or nr >= h or nc < 0 or nc >= w:
            continue
        if grid[nr][nc] == "#":
            continue
        ncell = nr * w + nc
        # ns = ncell * 4 + d と同じ。
        # (ncell << 2) で下位2bitを空け、| d で方向を詰める。
        # こうして「次状態」を整数1個で表す。
        ns = (ncell << 2) | d
        if parent[ns] != -2:
            continue
        parent[ns] = -1
        move_dir[ns] = d
        q.append(ns)

    goal_state = -1
    head = 0

    # ------------------------------------------------------------
    # 4) 拡張状態上で BFS
    # ------------------------------------------------------------
    while head < len(q):
        s = q[head]
        head += 1

        # s は (cell, dir) を1つに詰めた状態ID。
        cell = s >> 2
        # 下位2bitだけ取り出して直前方向を得る（0..3）。
        dprev = s & 0b11

        # どの直前方向でも G マスに着いたら終了
        if cell == g_idx:
            goal_state = s
            break

        r, c = divmod(cell, w)
        ch = grid[r][c]

        # 現在マスのルールから、次に選べる方向を決める
        if ch == "o":
            # 同じ方向のみ
            cand = (dprev,)
        elif ch == "x":
            # 同じ方向は禁止（反転して戻るのは可）
            if dprev == 0:
                cand = (1, 2, 3)
            elif dprev == 1:
                cand = (0, 2, 3)
            elif dprev == 2:
                cand = (0, 1, 3)
            else:
                cand = (0, 1, 2)
        else:
            # '.', 'S', 'G' は4方向すべて可
            cand = (0, 1, 2, 3)

        # 隣接マスへの遷移を試す
        for nd in cand:
            nr = r + dr[nd]
            nc = c + dc[nd]
            if nr < 0 or nr >= h or nc < 0 or nc >= w:
                continue
            if grid[nr][nc] == "#":
                continue
            ncell = nr * w + nc
            # ns = ncell * 4 + nd と同じ（状態のエンコード）。
            # ns を配列添字として使って訪問判定・親記録を行う。
            ns = (ncell << 2) | nd
            if parent[ns] != -2:
                continue
            parent[ns] = s
            move_dir[ns] = nd
            q.append(ns)

    if goal_state == -1:
        print("No")
        return

    # ------------------------------------------------------------
    # 5) 経路復元
    #    goal から parent をたどって -1（開始印）まで戻り、
    #    方向文字を逆順で集めて最後に反転する。
    # ------------------------------------------------------------
    path = []
    cur = goal_state
    while cur != -1:
        path.append(dir_char[move_dir[cur]])
        cur = parent[cur]
    path.reverse()

    # 有効な経路なら何でもよい（最短化は不要）。
    print("Yes")
    print("".join(path))


if __name__ == "__main__":
    main()
