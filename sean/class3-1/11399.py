from functools import reduce
import sys

# sys.stdin = open("input.txt", "r")

n = int(input())

p_list = sorted(map(int, input().split()))
acc = [0]
for i in range(len(p_list)):
    acc.append(acc[i] + p_list[i])

print(sum(acc[1:]))
