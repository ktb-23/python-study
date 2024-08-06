import sys
from collections import deque

# sys.stdin = open("input.txt", "r")

n = int(input())

custom_queue = deque()

for _ in range(n):
    command = input().split()
    if command[0] == "push":
        custom_queue.append(int(command[1]))
    elif command[0] == "pop":
        print(custom_queue.popleft()) if len(custom_queue) > 0 else print(-1)
    elif command[0] == "size":
        print(len(custom_queue))
    elif command[0] == "empty":
        print(1 if len(custom_queue) == 0 else 0)
    elif command[0] == "front":
        print(custom_queue[0]) if len(custom_queue) > 0 else print(-1)
    elif command[0] == "back":
        print(custom_queue[-1]) if len(custom_queue) > 0 else print(-1)
