import sys
input = sys.stdin.readline

def main():
    A = input()
    N = int(input())

    cnt = 0
    for i in N:
        for j in len(A):
            if A[i] == A[-i]:
                cnt +=1

    print(cnt)


if __name__ == "__main__":
    main()
