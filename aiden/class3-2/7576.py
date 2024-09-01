from collections import deque
import sys

input = sys.stdin.read
data = input().split()

m, n = map(int, data[0:2])

box = []
index = 2
for i in range(n):
    row = list(map(int,data[index:index + m]))
    box.append(row)
    index += m

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
            box[nx][ny] = box[x][y] + 1
            queue.append((nx, ny))

max_days = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            sys.exit(0)
        max_days = max(max_days, box[i][j])

print(max_days - 1)
