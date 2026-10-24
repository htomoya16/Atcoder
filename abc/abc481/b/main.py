import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n-1):
        if i > 0 and a[i] == k:
            cnt -=1
        b = sorted([a[i], a[i+1]])
        if k >= b[0] and k <= b[1]:
            cnt +=1

    print(cnt)

if __name__ == "__main__":
    main()
