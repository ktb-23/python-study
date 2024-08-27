import sys

# sys.stdin = open("input.txt", "r")

a, b, c = map(int, input().split())

answer = 1
current = a % c
order = 0

while (1 << order) <= b:
    if b & (1 << order):
        answer *= current
        answer %= c
    current *= current % c
    current %= c
    order += 1

print(answer)
