import sys
input = sys.stdin.readline

def is_palindrome_in_base(x: int, base: int) -> bool:
    original = x
    reversed_value = 0
    while x > 0:
        reversed_value = reversed_value * base + (x % base)
        x //= base
    return original == reversed_value


def main():
    A = int(input())
    N = int(input())

    ans = 0

    # N <= 10^12 なので、十進回文は「前半」を 1..999999 まで作れば十分。
    for half in range(1, 1_000_000):
        s = str(half)

        # 奇数桁回文 (例: 123 -> 12321)
        odd_pal = int(s + s[-2::-1])
         # 偶数桁回文 (例: 123 -> 123321)
        even_pal = int(s + s[::-1])

        if odd_pal > N and even_pal > N:
            break

        if odd_pal <= N and is_palindrome_in_base(odd_pal, A):
            ans += odd_pal
        if even_pal <= N and is_palindrome_in_base(even_pal, A):
            ans += even_pal

    print(ans)


if __name__ == "__main__":
    main()
