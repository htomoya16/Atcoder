import sys

input = sys.stdin.readline


def main():
    n, q = map(int, input().split())

    block = [[] for _ in range(n)]
    block_num = []
    flag_num = 0

    for _ in range(q):
        t, q = map(int, input().split())

        if t == 1:
            if len(block[q][0]) == 0:
                flag_num += 1
            block[q].append(True)
            if flag_num == n:
                for i in range(block):
                    block[i].pop()
        else:
            pass


if __name__ == "__main__":
    main()
