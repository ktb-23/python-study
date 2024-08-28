import sys

# sys.stdin = open("input.txt", "r")

lines = sys.stdin.readlines()
for line in lines:
  a, b = map(int, line.split())
  if a == 0 and b == 0:
    break
  print(a + b)