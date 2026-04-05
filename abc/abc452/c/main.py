import sys
from copy import deepcopy

input = sys.stdin.readline


def main():
    N = int(input())
    AB = {}
    for i in range(N):
        A, B = map(int, input().split())
        AB.setdefault(A, []).append(B)

    M = int(input())

    S_l = []
    char = []
    for i in range(M):
        s = input().split()
        S_l.append(s[0])
        for k, v in AB.items():
            if k == len(s[0]):
                for c in v:
                    char.append(s[0][c - 1])
                break

    for s in S_l:
        char_cp = deepcopy(char)
        ok = True
        for i in s:
            if i in char_cp:
                char_cp.remove(i)
                continue
            else:
                ok = False
                print("No")
                break
        if ok:
            print("Yes")


if __name__ == "__main__":
    main()
