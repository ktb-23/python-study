import sys
from collections import deque

def min_days(box, n, m):
    # 상하좌우 이동을 위한 좌표
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque()  # deque 생성
    yet_tomatoes = 0  # 아직 익지 않은 토마토(0) 카운트
    
    # 익은 토마토(1)를 큐에 넣고, 익지 않은 토마토(0)의 개수 세기
    for i in range(n):  # 세로 n
        for j in range(m):  # 가로 m
            if box[i][j] == 1:  # 해당 칸이 익은 토마토라면
                queue.append((i, j))  # 해당 토마토 위치 저장
            elif box[i][j] == 0:  # 해당 칸이 익지 않은 토마토라면
                yet_tomatoes += 1
    
    # 처음부터 익지 않은 토마토가 없다면 0 출력
    if yet_tomatoes == 0:
        return 0
    
    # BFS로 토마토 후숙 최소 일수 탐색
    days = -1  # +1 하면서 시작할 것이므로
    while queue:
        days += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            
            # 상하좌우로 토마토가 익을 수 있는지 확인
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # 범위 내의 익지 않은 토마토라면 익게 하기
                if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                    box[nx][ny] = 1  # 익음(1)
                    yet_tomatoes -= 1
                    queue.append((nx, ny))
                    
    # 모든 토마토가 익었는지 확인
    if yet_tomatoes == 0:
        return days
    else:  # 토마토가 모두 익지는 못하는 상황
        return -1


# 입력 처리
input = sys.stdin.read
data = input().strip().splitlines()

# 첫째 줄: 상자를 크기를 나타내는 두 정수 M, N (2 ≤ M,N ≤ 1,000)
M, N = map(int, data[0].split())  # 상자 가로 칸 수 M, 세로 칸 수 N

# 다음 n줄: 하나의 상자에 저장된 토마토들의 정보  1, 0, -1
box = [list(map(int, line.split())) for line in data[1:N+1]]

# 출력 결과 (토마토가 모두 익을 때까지의 최소 날짜)
output = str(min_days(box, N, M))
sys.stdout.write(output + '\n')