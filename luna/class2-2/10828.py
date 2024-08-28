import sys

input = sys.stdin.read
data = input().splitlines()
commands = data[1:]

def stack_commands(commands):
    stack = []
    output = []
    
    for command in commands:
        if command.startswith("push"):
            _, value = command.split()
            stack.append(int(value))
        elif command == "pop":
            output.append(stack.pop() if stack else -1)
        elif command == "size":
            output.append(len(stack))
        elif command == "empty":
            output.append(1 if not stack else 0)
        elif command == "top":
            output.append(stack[-1] if stack else -1)
    return output

result = "\n".join(map(str,stack_commands(commands)))
sys.stdout.write(result + '\n')