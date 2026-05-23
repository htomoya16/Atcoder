import sys

input = sys.stdin.readline


def main():
    n = int(input())
    s = input().split()

    ans = []
    for string in s:
        s_int = ord(string[0])
        if s_int >= ord("a") and s_int <= ord("o"):
            ans.append((s_int - ord("a") + 3) // 3 + 1)
        elif s_int >= ord("p") and s_int <= ord("s"):
            ans.append(7)
        elif s_int >= ord("t") and s_int <= ord("v"):
            ans.append(8)
        elif s_int >= ord("w") and s_int <= ord("z"):
            ans.append(9)

    print("".join(str(s) for s in ans))


if __name__ == "__main__":
    main()
