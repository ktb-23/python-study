import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
meetings = []

for i in range(n):
    start = int(data[2 * i + 1])
    end = int(data[2 * i + 2])
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end_time = 0

for start, end in meetings:
    if start >= last_end_time:
        last_end_time = end
        count += 1

print(count)