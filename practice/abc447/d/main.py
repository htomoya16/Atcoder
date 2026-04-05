import sys

input = sys.stdin.readline


def main():
    S = input().strip()
    a_cnt = 0
    b_cnt = 0
    c_cnt = 0

    for c in S:
        if c == "A":
            a_cnt += 1
        elif c == "B" and b_cnt < a_cnt:
            b_cnt += 1
        elif c == "C" and c_cnt < b_cnt:
            c_cnt += 1
    print(c_cnt)


if __name__ == "__main__":
    main()
