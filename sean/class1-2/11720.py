import sys
from functools import reduce

# sys.stdin = open("input.txt", "r")

_ = int(input())
print(reduce(lambda acc, cur: acc + cur, map(int, input().strip())))
