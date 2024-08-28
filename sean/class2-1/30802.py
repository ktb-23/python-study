import sys
from functools import reduce

# sys.stdin = open("input.txt", "r")

n = int(input())
shirts_sizes = list(map(int, input().split()))
t, p = map(int, input().split())

shirts_bundle_count = reduce(
    lambda acc, shirts_count: acc + (shirts_count // t) + ((shirts_count % t) and 1),
    shirts_sizes, 0
)

print(shirts_bundle_count)
print(f"{n // p} {n % p}")
