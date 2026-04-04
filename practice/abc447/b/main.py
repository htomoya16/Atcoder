import sys

input = sys.stdin.readline


def main():
    S = input()

    S_dict = {S[i]: S.count(S[i]) for i in range(len(S))}

    S_max = max(S_dict.values())
    for s, cnt in S_dict.items():
        if cnt == S_max:
            S = S.replace(s, "")
    S = S.replace("\n", "")
    print(S)


if __name__ == "__main__":
    main()
