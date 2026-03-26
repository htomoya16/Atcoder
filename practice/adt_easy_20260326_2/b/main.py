import sys
input = sys.stdin.readline

def f(k):
    if k == 0:
        return 1
    return k * f(k -1)

def main():
    N = int(input())

    print(f(N))

if __name__ == "__main__":
    main()