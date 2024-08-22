import sys

# sys.stdin = open("input.txt", "r")

test_case = int(input())
for _ in range(test_case):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(stickers[0][0], stickers[1][0]))
        continue

    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = stickers[0][0]
    dp[0][1] = stickers[1][0]
    dp[1][0] = dp[0][1] + stickers[0][1]
    dp[1][1] = dp[0][0] + stickers[1][1]

    for i in range(2, n):
        dp[i][0] = max(dp[i - 1][1], dp[i - 2][1]) + stickers[0][i]
        dp[i][1] = max(dp[i - 1][0], dp[i - 2][0]) + stickers[1][i]

    print(max(dp[-1]))
