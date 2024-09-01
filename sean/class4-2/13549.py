from collections import deque
import sys

# sys.stdin = open("input.txt", "r")

n, k = map(int, input().split())

MAX_POS = 200000

dp = [MAX_POS + 1] * (MAX_POS + 1)

queue = deque([n])
dp[n] = 0

while queue:
    x = queue.popleft()
    if x != 0 and dp[x - 1] > dp[x] + 1:
        dp[x - 1] = dp[x] + 1
        queue.append(x - 1)
    if x + 1 <= MAX_POS and dp[x + 1] > dp[x] + 1:
        dp[x + 1] = dp[x] + 1
        queue.append(x + 1)
    if 2 * x <= MAX_POS and dp[2 * x] > dp[x]:
        dp[2 * x] = dp[x]
        queue.append(2 * x)

print(dp[k])
