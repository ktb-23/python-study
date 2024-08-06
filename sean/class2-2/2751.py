import sys

# sys.stdin = open("input.txt", "r")

n = int(input())
lines = sys.stdin.readlines()
numbers = sorted(list(map(int, lines)))
print("\n".join(map(str, numbers)))
