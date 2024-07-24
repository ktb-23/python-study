import sys

# sys.stdin = open("input.txt", "r")

for line in sys.stdin.readlines():
  a, b = map(int, line.split())
  print(a + b)