import sys

# sys.stdin = open("input.txt", "r")

n, k = map(int, input().split())

items = sorted(
    [list(map(int, input().split())) for _ in range(n)],
    key=lambda x: x[1] / x[0],
    reverse=True,
)

dp = [0] * (k + 1)

answer = 0
for weight, price in items:
    for i in range(k, weight - 1, -1):
        if i - weight >= 0:
            dp[i] = max(dp[i], dp[i - weight] + price)
            answer = max(answer, dp[i])

print(answer)
