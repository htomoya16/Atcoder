import sys

input = sys.stdin.readline


def main() -> None:
    s = input().strip()

    rs = s[::-1]
    words = ["dream", "dreamer", "erase", "eraser"]
    rev_words = [w[::-1] for w in words]

    i = 0
    n = len(rs)
    while i < n:
        matched = False
        for w in rev_words:
            if rs.startswith(w, i):
                i += len(w)
                matched = True
                break
        if not matched:
            print("NO")
            return

    print("YES")


if __name__ == "__main__":
    main()
