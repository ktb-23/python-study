import sys

# sys.stdin = open("input.txt", "r")

memo = [1, 2]

for i in range(2, 1001):
    memo.append((memo[i - 1] + memo[i - 2]) % 10007)

n = int(input())
print(memo[n - 1])
