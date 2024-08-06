import sys

input = sys.stdin.read
data = input().splitlines()
num_T = int(data[0])
data_PS = data[1:]

results = []

for expression in data_PS:
    is_valid = True
    stack = []
    
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                is_valid = False
                break
            else:
                stack.pop()
                
    if is_valid and not stack:
        results.append('YES')
    else:
        results.append('NO')

output = "\n".join(results)
sys.stdout.write(str(output) + '\n')