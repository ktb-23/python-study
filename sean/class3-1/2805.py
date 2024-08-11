from functools import reduce
import sys

# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = -1
end = 1000000001

while start + 1 < end:
    mid = (start + end) // 2
    cuuted_tree = reduce(
        lambda acc, cur: acc + cur - mid if cur - mid > 0 else acc, trees, 0
    )
    if cuuted_tree >= m:
        start = mid
    else:
        end = mid

print(start)
