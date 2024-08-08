import sys

# sys.stdin = open("input.txt", "r")

t = int(input())

memo = [-1, 1, 2, 4]
for _ in range(4, 12):
    memo.append(sum(memo[-3:]))

for _ in range(t):
    print(memo[int(input())])
