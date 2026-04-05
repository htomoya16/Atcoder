import sys

input = sys.stdin.readline


def main():
    H, W = map(int, input().split())

    wr = []
    for i in range(H):
        if i == 0 or i == H - 1:
            print("".join("#" for _ in range(W)))
        else:
            print("#" + "." * (W - 2) + "#")


if __name__ == "__main__":
    main()
