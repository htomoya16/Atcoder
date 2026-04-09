import sys

input = sys.stdin.readline


def main():
    H, W, N = map(int, input().split())

    YX = [1, 1]

    H_d = {}
    W_d = {}

    for _ in range(N):
        h, w = map(int, input().split())

        H_d.setdefault(h, [])
        W_d.setdefault(w, [])

        H_d[h].append(w)
        W_d[w].append(h)

    while True:
        if len(H_d) == 0:
            break
        if H_d.get(H) and H_d.get(H) != []:
            w = H_d[H].pop()
            if H_d[H] == []:
                H_d.pop(H)
            W_d[w].remove(H)
            if W_d[w] == []:
                W_d.pop(w)
            W -= w
            print(YX[0], YX[1])
            YX[1] += w
            continue
        elif W_d.get(W) and W_d.get(W) != []:
            h = W_d[W].pop()
            if W_d[W] == []:
                W_d.pop(W)
            H_d[h].remove(W)
            if H_d[h] == []:
                H_d.pop(h)
            H -= h
            print(YX[0], YX[1])
            YX[0] += h
            continue


if __name__ == "__main__":
    main()
