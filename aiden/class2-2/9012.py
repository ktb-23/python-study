import sys


input = sys.stdin.readline

t = int(input().strip())  
vps_list = [input().strip() for _ in range(t)]

for vps in vps_list:
    stack=[]
    answer = True
    for char in vps:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                answer = False
                break
    if answer and not stack:
        print('YES')
    else:
        print('NO')