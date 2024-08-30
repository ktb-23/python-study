import sys

# sys.stdin = open("input.txt", "r")

n = int(input())

tree = [list(map(int, input().split())) for _ in range(n)]

dp = [([0] * i) for i in range(1, n + 1)]
dp[0][0] = tree[0][0]

for i in range(1, n):
    for j in range(i + 1):
        left = dp[i - 1][j - 1] if j != 0 else 0
        right = dp[i - 1][j] if j != i else 0
        dp[i][j] = tree[i][j] + max(left, right)

print(max(dp[n - 1]))
