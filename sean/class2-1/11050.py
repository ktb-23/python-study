from math import comb
import sys

# sys.stdin = open("input.txt", "r")

[n, k] = map(int, input().split())

print(comb(n, k))
