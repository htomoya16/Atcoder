import sys
input = sys.stdin.readline

def main():
    data = [int(c) for c in input().split()]
    # dataの中で隣り合う等しい要素が存在するなら"YES"を出力し、そうでなければ"NO"を出力する
    # ここにプログラムを追記
    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            print("YES")
            break
    else:
        print("NO")



if __name__ == "__main__":
    main()