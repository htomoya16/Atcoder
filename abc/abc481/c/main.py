import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    q_t = int(input())
    d = defaultdict()
    cnt = 0
    for i in range(q_t):
        q = input()

        if d.get(q):
            print(d[q])
            continue
        else:
            cnt += 1
            d[q] = cnt
            print(cnt)



if __name__ == "__main__":
    main()
