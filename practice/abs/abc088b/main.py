import sys

input = sys.stdin.readline


def main():
    n = int(input())
    a = sorted(map(int, input().split()))
    a.reverse()

    for i in range(n):
        if i % 2 == 1:
            a[i] *= -1
    print(sum(a))


if __name__ == "__main__":
    main()
