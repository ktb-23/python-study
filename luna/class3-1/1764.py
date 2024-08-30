import sys

input = sys.stdin.read
data = input().splitlines()

num_N, num_M = map(int, data[0].split())
set_H = set(data[1:num_N + 1])  # couldn't hear
set_S = set(data[num_N + 1:])  # couldn't see


set_HS = sorted(set_S.intersection(set_H))
result = [str(len(set_HS))] + set_HS


output = "\n".join(f"{x}" for x in result)
sys.stdout.write(output + '\n')