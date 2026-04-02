import sys

input = sys.stdin.readline


def main():
    choco = [None, None]
    choco[0], choco[1], Q = map(int, input().split())

    for i in range(Q):
        t, q = map(int, input().split())
        if t == 1:
            print(choco[1] * q)
            choco[0] -= q
        if t == 2:
            print(choco[0] * q)
            choco[1] -= q


if __name__ == "__main__":
    main()
