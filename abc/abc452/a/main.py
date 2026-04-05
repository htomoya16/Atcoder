import sys

input = sys.stdin.readline


def main():
    M, D = map(int, input().split())

    a = [[1, 7], [3, 3], [5, 5], [7, 7], [9, 9]]

    ok = False
    for m, d in a:
        if M == m and D == d:
            ok = True
            print("Yes")
    if not ok:
        print("No")


if __name__ == "__main__":
    main()
