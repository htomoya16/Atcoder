import sys

input = sys.stdin.readline


def main():
    H, W = map(int, input().split())

    S = [[None for _ in range(W)] for _ in range(H)]

    for i in range(H):
        s = input().strip()
        for j in range(W):
            S[i][j] = s[j]

    w1, w2 = 0, 0
    h1, h2 = 0, 0
    ans = 0

    for h1 in range(H):
        for w1 in range(W):
            for h2 in range(h1, H - h1):
                for w2 in range(w1, W - w1):
                    ok = True
                    for i in range(h1, h2):
                        for j in range(w1, w2):
                            # print(i, j, h1, h2, w1, w2, h1 + h2 - i, w1 + w2 - j)
                            if S[i][j] != S[h1 + h2 - i][w1 + w2 - j]:
                                ok = False
                                break
                        if not ok:
                            break
                    if ok:
                        # print(h1, h2, w1, w2)
                        ans += 1
    # print(S)
    print(ans)


if __name__ == "__main__":
    main()
