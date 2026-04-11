import sys

input = sys.stdin.readline


def main():
    N = int(input())
    S = input().strip()

    cnt = 0
    for i in range(N):
        if S[i] != "o":
            cnt = i
            break
        if i == N - 1:
            cnt = -1

    if cnt < 0:
        print("")
    else:
        print(S[cnt:])


if __name__ == "__main__":
    main()
