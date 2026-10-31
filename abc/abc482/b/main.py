import sys
input = sys.stdin.readline

def main():
    s_list = list()
    row = list()
    for i in range(5):
        s = input().strip()
        s_list.append(s)
        row.append(s.count("."))

    max_cnt = 5
    for i in range(5):
        cnt = 0
        for j in range(5):
            if s_list[j][i] == ".":
                cnt += 1
        max_cnt = min(max_cnt, cnt, row[i])
    naname1_cnt = 0
    naname2_cnt = 0
    for i in range(5):
        if s_list[i][i] == ".":
            naname1_cnt += 1
        if s_list[5-i-1][i] == ".":
            naname2_cnt += 1
    max_cnt = min(max_cnt, naname1_cnt, naname2_cnt)
    print(max_cnt)






if __name__ == "__main__":
    main()
