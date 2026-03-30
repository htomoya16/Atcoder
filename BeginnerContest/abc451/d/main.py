import sys

from sortedcontainers import SortedSet

input = sys.stdin.readline


def main():
    N = int(input())
    num = SortedSet()

    i = 0
    dict = 1
    while True:
        # 答え
        if dict > len(str(N)):
            print(num[N - 1])
            return
        while True:
            num.add(pow(2, i))
            if len(str(num[-1])) > dict:
                break

        i += 1
        s = str(num[-1])

        if len(s) != dict:
            dict += 1
            for i in num:
                for j in num:
                    make_num = str(i) + str(j)
                    if len(make_num) > dict:
                        break
                    num.add(int(make_num))
                if len(str(i)) >= dict:
                    break


if __name__ == "__main__":
    main()
