import sys
from collections import defaultdict, deque

input = sys.stdin.read
data = input().split()

n = int(data[0])
num_pair = int(data[1])
connect = defaultdict(list)
index = 2

for _ in range(num_pair):
    com1 = int(data[index])
    com2 = int(data[index+1])
    connect[com1].append(com2)
    connect[com2].append(com1)
    index += 2

def bfs(start):
    visited = set()
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.add(current)
            queue.extend(connect[current])
    
    return len(visited) - 1

result = bfs(1)
print(result)