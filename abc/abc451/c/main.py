import sys

from sortedcontainers import SortedList

input = sys.stdin.readline


def main():
    Q = int(input())

    woods = SortedList()

    for i in range(Q):
        q, h = map(int, input().split())
        if q == 1:
            woods.add(h)
        elif q == 2:
            for j in range(woods.bisect_right(h)):
                woods.pop(0)
        print(len(woods))


if __name__ == "__main__":
    main()
