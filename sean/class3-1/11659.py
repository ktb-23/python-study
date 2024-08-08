from itertools import accumulate
import sys

# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
numbers = [0]
numbers.extend(map(int, input().split()))
numbers_acc = list(accumulate(numbers))

for _ in range(m):
    start, end = map(int, input().split())
    print(numbers_acc[end] - numbers_acc[start - 1])
