import sys

# sys.stdin = open("input.txt", "r")

n = int(input())
set_a = set(map(int, input().split()))
m = int(input())
targets = map(int, input().split())
for x in targets:
    print(1 if x in set_a else 0)
