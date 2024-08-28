from math import gcd
import sys

# sys.stdin = open("input.txt", "r")

[a, b] = map(int, input().split())

gcd_value = gcd(a, b)
lcm_value = a * b / gcd_value

print(gcd_value)
print(int(lcm_value))