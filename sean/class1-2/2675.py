import sys

# sys.stdin = open("input.txt", "r")

test_case = int(input())

for _ in range(test_case):
  r, s = input().split()
  r = int(r)
  
  # string은 iterable
  print(''.join(list(map(lambda c: c*r, s))))