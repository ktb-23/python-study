import sys

input = sys.stdin.read
data = input().splitlines()

num_set_A = int(data[0])
nums_set_A = set(map(int, data[1].split()))
num_set_B = int(data[2])
nums_set_B = list(map(int, data[3].split()))
result = []

for num in nums_set_B:
    if num in nums_set_A:
        result.append(1)
    else:
        result.append(0)

output = "\n".join(f"{x}" for x in result)
sys.stdout.write(output + '\n')