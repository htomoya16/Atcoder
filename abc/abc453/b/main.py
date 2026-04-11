import sys

input = sys.stdin.readline


def main():
    T, X = map(int, input().split())
    A = list(map(int, input().split()))

    i = 0
    past = 0
    for t in range(T + 1):
        if t == 0 and past == 0:
            print(t, A[i])
            past = A[i]

        if abs(past - A[i]) >= X:
            past = A[i]
            print(t, A[i])

        i += 1


if __name__ == "__main__":
    main()
