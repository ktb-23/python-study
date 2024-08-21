import sys

# sys.stdin = open("input.txt", "r")

n = int(input())

meeting_times = sorted(
    [list(map(int, input().split())) for _ in range(n)], key=lambda x: (x[1], x[0])
)

answer = 0
current_time = 0
for start, end in meeting_times:
    if start >= current_time:
        current_time = end
        answer += 1

print(answer)
