import sys

data = sys.stdin.read().split()
n = int(data[0])
index = 1
houses=[]

for _ in range(n):
    house_list = list(map(int,data[index:index+3]))
    houses.append(house_list)
    index += 3

dp = [[0] * 3 for _ in range(1000)]

# 빨강 집
dp[0][0] = houses[0][0]
# 파랑 집
dp[0][1] = houses[0][1]
# 초록 집
dp[0][2] = houses[0][2]

for i in range(n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + houses[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + houses[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + houses[i][2]

answer = min(dp[n-1][0], dp[n-1][1], dp[n-1][2])
print(answer)
