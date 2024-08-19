import sys

input = sys.stdin.read
data = input().splitlines()

num_N = int(data[0])
list_time = sorted(map(int, data[1].split()))

for i in range(1, num_N):
    list_time[i] += list_time[i - 1]

total_time = sum(list_time)

sys.stdout.write(str(total_time) + '\n')