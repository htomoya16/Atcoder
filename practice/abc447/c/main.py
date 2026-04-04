import sys

input = sys.stdin.readline


def main():
    S = input()
    T = input()

    ans = 0
    i = 0
    if S.replace("A", "") != T.replace("A", ""):
        print(-1)
        exit()
    while True:
        if S == T:
            break
        S_index = min(i, len(S) - 1)
        T_index = min(i, len(T) - 1)

        while S[S_index] != T[T_index]:
            ans += 1
            if S[S_index] == "A":
                S = S[:S_index] + S[S_index + 1 :]
            else:
                T = T[:T_index] + T[T_index + 1 :]
        i += 1

    print(ans)


if __name__ == "__main__":
    main()
