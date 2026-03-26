import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    a = list(map(int, input().split()))


    ret = list()
    tmp = list()
    j = 0
    for i in range(1, N+1):
        if i == a[j]:
            j += 1
            tmp.append(i)
        else:
            tmp.reverse()
            ret += tmp
    print(*ret)

if __name__ == "__main__":
    main()