import sys

input = sys.stdin.readline


def main():
    H, W = map(int, input().split())
    S = [input().strip() for _ in range(H)]

    ans = 0
    for h1 in range(H):
        for h2 in range(h1, H):
            for w1 in range(W):
                for w2 in range(w1, W):
                    ok = True
                    for i in range(h1, h2 + 1):
                        for j in range(w1, w2 + 1):
                            ni = h1 + h2 - i
                            nj = w1 + w2 - j
                            if S[i][j] != S[ni][nj]:
                                ok = False
                                break
                        if not ok:
                            break
                    if ok:
                        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
