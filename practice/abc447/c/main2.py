import sys

input = sys.stdin.readline


def main():
    S = input()
    T = input()

    ans = 0
    if S.replace("A", "") != T.replace("A", ""):
        print(-1)
        exit()
    i = 0
    j = 0
    while True:
        if i >= len(S):
            break
        while True:
            if j >= len(T):
                break
            if S[i] == S[j]:
                i += 1
                j += 1
                continue
            ans += 1
            if S[i] == "A":
                i += 1
            else:
                j += 1
    print(ans)


if __name__ == "__main__":
    main()
