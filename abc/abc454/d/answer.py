import sys

input = sys.stdin.readline


def normalize(s: str) -> str:
    st = []
    for ch in s:
        st.append(ch)
        while (
            len(st) >= 4
            and st[-4] == "("
            and st[-3] == "x"
            and st[-2] == "x"
            and st[-1] == ")"
        ):
            st.pop()
            st.pop()
            st.pop()
            st.pop()
            st.append("x")
            st.append("x")
    return "".join(st)


def main() -> None:
    t = int(input())
    out = []
    for _ in range(t):
        a = input().strip()
        b = input().strip()
        out.append("Yes" if normalize(a) == normalize(b) else "No")
    print("\n".join(out))


if __name__ == "__main__":
    main()
