import sys

input = sys.stdin.readline


def main():
    S = input().strip()
    if S[0] == S[-1]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
