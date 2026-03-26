import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))

    if N < 2:
        print("No")
        return
    r = A[1] / A[0]

    for i, v in enumerate(A):
        if i == 0:
            continue
        if v != r * A[i-1]:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()