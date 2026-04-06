import sys

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())

    zaiko = [True] * M

    for i in range(N):
        L = int(input())
        X = list(map(int, input().split()))
        for x in X:
            if zaiko[x - 1]:
                print(x)
                zaiko[x - 1] = False
                break
        else:
            print(0)


if __name__ == "__main__":
    main()
