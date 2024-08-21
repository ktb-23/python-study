from collections import deque
import sys

# sys.stdin = open("input.txt", "r")

custom_deque = deque()

custom_deque.append((int(input()), 0))

while custom_deque:
    x, n = custom_deque.popleft()
    if x == 1:
        print(n)
        break
    if x % 3 == 0:
        custom_deque.append((x // 3, n + 1))
    if x % 2 == 0:
        custom_deque.append((x // 2, n + 1))
    custom_deque.append((x - 1, n + 1))
