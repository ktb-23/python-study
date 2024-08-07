import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()
commands = data[1:]

def deque_commands(commands):
    queue = deque()
    output = []
    
    for command in commands:
        if command.startswith("push"):
            _, value = command.split()
            queue.append(int(value))
        elif command == "pop":
            output.append(queue.popleft() if queue else -1)
        elif command == "size":
            output.append(len(queue))
        elif command == "empty":
            output.append(1 if not queue else 0)
        elif command == "front":
            output.append(queue[0] if queue else -1)
        elif command == "back":
            output.append(queue[-1] if queue else -1)
    return output

result = "\n".join(map(str,deque_commands(commands)))
sys.stdout.write(result + '\n')