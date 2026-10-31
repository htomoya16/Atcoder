import sys
input = sys.stdin.readline

def main():
    s = input().strip()

    cnt = s.count("o")

    if cnt %2 == 0:
        print("even")
    else:
        print("odd")

if __name__ == "__main__":
    main()
