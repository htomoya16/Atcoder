import sys

input = sys.stdin.readline


def main():
    n = int(input())
    moti = set()

    for i in range(n):
        d = int(input())
        moti.add(d)
    print(len(moti))


if __name__ == "__main__":
    main()
