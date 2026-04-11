import sys

input = sys.stdin.readline


def main():
    N = int(input())
    L = list(map(int, input().split()))

    zahyo = 0.5
    cnt = 0
    for l in L:
        past = zahyo
        if zahyo > 0:
            zahyo -= l
        else:
            zahyo += l
        if past * zahyo < 0:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
