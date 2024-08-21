from collections import deque
from math import inf
import sys

# sys.stdin = open("input.txt", "r")

subin, target = map(int, input().split())
flag = {}
flag[subin] = True

que = deque([(subin, 0)])
while True:
    current, spend_time = que.popleft()
    if current == target:
        print(spend_time)
        break
    if current + 1 <= 100000 and not flag.get(current + 1):
        flag[current + 1] = True
        que.append((current + 1, spend_time + 1))
    if current - 1 >= 0 and not flag.get(current - 1):
        flag[current - 1] = True
        que.append((current - 1, spend_time + 1))
    if current * 2 <= 100000 and not flag.get(current * 2):
        flag[current * 2] = True
        que.append((current * 2, spend_time + 1))
