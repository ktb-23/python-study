from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and field[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input()) 

for _ in range(t):
    m, n, k = map(int, input().split())  
    field = [[0] * m for _ in range(n)]  
    visited = [[False] * m for _ in range(n)]  
    
    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1
    
    count = 0  
    
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                count += 1
    
    print(count)
