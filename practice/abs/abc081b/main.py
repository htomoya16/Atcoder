import sys

input = sys.stdin.readline


def main():
    n = int(input())
    a = list(map(int, input().split()))

    cnt = 0
    while True:
        ok = True

        for i in range(n):
            if a[i] % 2 == 1:
                ok = False
                break
        if ok:
            cnt += 1
            a = [i // 2 for i in a]
        else:
            break
    print(cnt)


if __name__ == "__main__":
    main()
