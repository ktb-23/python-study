import sys
from functools import reduce

# sys.stdin = open("input.txt", "r")

def getBiggerNumber(a, i):
  b = int(input()), i
  return a if (a[0] > b[0]) else b

answer = reduce(getBiggerNumber, range(1, 10), [0, -1])

print(answer[0])
print(answer[1])