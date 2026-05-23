StoC = "22233344455566677778889999"
ans = ""
n = int(input())
s = list(input().split())
for i in range(n):
    ans += StoC[ord(s[i][0]) - ord("a")]
print(ans)
