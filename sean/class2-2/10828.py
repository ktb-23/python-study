import sys

# sys.stdin = open("input.txt", "r")

n = int(input())

custom_stack = []

for _ in range(n):
    command = input().split()
    if command[0] == "push":
        custom_stack.append(int(command[1]))
    elif command[0] == "pop":
        print(custom_stack.pop()) if len(custom_stack) > 0 else print(-1)
    elif command[0] == "size":
        print(len(custom_stack))
    elif command[0] == "empty":
        print(1 if len(custom_stack) == 0 else 0)
    elif command[0] == "top":
        print(custom_stack[-1]) if len(custom_stack) > 0 else print(-1)
