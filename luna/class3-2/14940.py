import sys
from collections import deque

def from_1_to_2(grid, n, m):  # 1에서 2까지 이동하는 거리를 찾는 함수
    # 상하좌우 이동을 위한 좌표
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 거리 저장용 배열, 갈 수 있는 땅(1)은 -1, 갈 수 없는 땅(0, 2)은 0으로 초기화
    distances = [[-1 if grid[i][j] == 1 else 0 for j in range(m)] for i in range(n)]

    queue = deque()  # 큐 초기화    

    # 목표 지점(2) 찾기
    for i in range(n):  # 세로 n
        for j in range(m):  # 가로 m
            if grid[i][j] == 2:  # 목표 지점(2)이라면
                queue.append((i, j))  # 해당 위치 저장, 목표지점 거리는 이미 0이므로 생략
                
    while queue:
        x, y = queue.popleft()
            
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 상하좌우에 아직 가지 않은 땅(dis -1)이 유효한 범위 내에 있다면
            if 0 <= nx < n and 0 <= ny < m and distances[nx][ny] == -1:
                distances[nx][ny] = distances[x][y] + 1 # 이전 위치의 거리 +1
                queue.append((nx, ny))  # 이동 및 큐에 새 좌표 추가

    return distances  # while 구문이 끝났을 때(queue에 아무것도 없을 때) 결과값 반환


# 입력 처리
input = sys.stdin.read
data = input().strip().splitlines()

# 첫째 줄: 지도의 크기 n, m (2 ≤ n, m ≤ 1,000)
n, m = map(int, data[0].split())  # 세로 n, 가로 m

# 다음 n줄: 한 줄마다의 땅 정보  0, 1, 2  (2는 land에서 한 개)
land = [list(map(int, line.split())) for line in data[1:n+1]]

# 출력 결과
result = from_1_to_2(land, n, m)
output = '\n'.join(' '.join(map(str, row)) for row in result)
sys.stdout.write(output + '\n')