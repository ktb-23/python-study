import sys
from collections import deque

input = sys.stdin.read
data = input().split()

n, m = int(data[0]), int(data[1])
grid = []
index = 2

for i in range(n):
    grid.append(list(map(int, data[index:index + m])))
    index += m

distance = [[-1] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

start_x, start_y = 0, 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            start_x, start_y = i, j
            break

queue = deque([(start_x, start_y)])
distance[start_x][start_y] = 0

while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and distance[nx][ny] == -1:
            distance[nx][ny] = distance[x][y] + 1
            queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            print(0, end=' ')
        elif distance[i][j] == -1:
            print(-1, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()
