import sys

input = sys.stdin.readline


def main():
    N, A, B = map(int, input().split())

    total = 0
    for n in range(1, N + 1):
        total_n = 0
        tmp = n
        while tmp > 0:
            total_n += tmp % 10
            tmp //= 10
        if total_n >= A and total_n <= B:
            total += n

    print(total)


if __name__ == "__main__":
    main()
