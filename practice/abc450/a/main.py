import sys

input = sys.stdin.readline


def main():
    N = int(input())
    a = []
    for i in range(N, 0, -1):
        a.append(str(i))
    result = ",".join(a)
    print(result)


if __name__ == "__main__":
    main()
