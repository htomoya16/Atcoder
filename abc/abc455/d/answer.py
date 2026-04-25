import sys

input = sys.stdin.readline


def main():
    N, Q = map(int, input().split())

    below = [0] * (N + 1)

    for _ in range(Q):
        C, P = map(int, input().split())
        below[C] = P

    def find_bottom(card):
        path = []
        while below[card] != 0:
            path.append(card)
            card = below[card]

        for x in path:
            below[x] = card

        return card

    ans = [0] * (N + 1)
    for card in range(1, N + 1):
        bottom = find_bottom(card)
        ans[bottom] += 1

    print(*ans[1:])


if __name__ == "__main__":
    main()
