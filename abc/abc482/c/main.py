import sys
import bisect
from sortedcontainers import SortedDict
from collections import defaultdict
input = sys.stdin.readline


def main():
    h, w, n, q = map(int, input().split())
    r_map = SortedDict()
    c_map = SortedDict()
    for _ in range(n):
        r, c = map(int, input().split())
        if r_map.get(r) == None:
            r_map[r] = 1
        if c_map.get(c) == None:
            c_map[c] = 1

    r_list = list()
    c_list = list()
    cnt = 0
    for k in r_map.keys():
        cnt += 1
        r_map[k] = cnt
        r_list.append(k)
    cnt = 0
    for k in c_map.keys():
        cnt += 1
        c_map[k] = cnt
        r_list.append(k)
    r_list = sorted(r_list)
    c_list = sorted(c_list)

    for i in range(q):
        num, q1, q2 = map(int, input().split())
        if num == 1:
            q1 =  bisect.bisect_left(r_list,q1)
            q2 = bisect.bisect_right(r_list,q2)
            print(r_map[q2]-r_map[q1])
        else:
            q1 =  bisect.bisect_left(c_list,q1)
            q2 = bisect.bisect_right(c_list,q2)
            print(c_map[q2]-c_map[q1])




if __name__ == "__main__":
    main()
