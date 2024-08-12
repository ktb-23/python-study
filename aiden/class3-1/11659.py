import sys

input = sys.stdin.read
data = input().split()

n, m = int(data[0]), int(data[1])
n_list = list(map(int, data[2:n+2]))

cum_sum = [0] * (n + 1)

for i in range(1, n + 1):
    cum_sum[i] = cum_sum[i - 1] + n_list[i - 1]

result = []
index = n + 2
for _ in range(m):
    i = int(data[index])
    j = int(data[index + 1])
    result.append(cum_sum[j] - cum_sum[i - 1])
    index += 2

sys.stdout.write("\n".join(map(str, result)) + "\n")
