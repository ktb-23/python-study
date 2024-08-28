import sys
from collections import deque

input = sys.stdin.read
data = input().split()
n = int(data[0])
queue = deque()

index = 1
for i in range(n):
    command = data[index]
    if command == 'push':
        queue.append(data[index+1])
        index += 2
        
    elif command == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
        index += 1
    
    elif command == 'size':
        print(len(queue))
        index += 1
    
    elif command == 'empty':
        print(0 if queue else 1)
        index += 1
    
    elif command == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
        index += 1
    
    elif command == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
        index += 1
