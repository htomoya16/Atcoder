import sys
input = sys.stdin.readline

def main():
    N = int(input())

    total = 0
    for i in range(N):
        total += pow(-1, i+1) * pow(i+1, 3)

    print(total)

if __name__ == "__main__":
    main()