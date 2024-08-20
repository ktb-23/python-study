import sys

# sys.stdin = open("input.txt", "r")

n = int(input())
sequence = list(map(int, input().split()))

memo = [(value, 1) for value in sequence]

answer = 1

for i in range(n):
    for j in range(i):
        max_value, count = memo[j]

        if max_value < sequence[i] and count >= memo[i][1]:
            memo[i] = (sequence[i], count + 1)
            answer = max(count + 1, answer)

print(answer)
