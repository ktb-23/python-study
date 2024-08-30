import sys

# 입력 처리
input = sys.stdin.read
data = input().strip().splitlines()

# 첫째 줄: 테스트 케이스의 개수 T
T = int(data[0])

# 방향 (상하좌우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# T개의 문단: 각각의 테스트 케이스
index = 1
results = []
for _ in range(T):
    # 문단의 첫째 줄: 배추밭의 가로길이 M, 세로길이 N, 배추 개수 K
    M, N, K = map(int, data[index].split())
    # 배추밭 초기화
    field = [[0] * M for _ in range(N)]
    # 다음 K줄: 배추의 위치 X, Y
    positions = [tuple(map(int, data[i + index + 1].strip().split())) for i in range(K)]
    # 배추 위치 표시
    for x, y in positions:
        field[y][x] = 1

    index += K + 1  # 다음 테스트 케이스를 위한 인덱스 설정

    # 지렁이 수 카운트
    worm_count = 0

    # BFS로 필요한 배추흰지렁이 수 탐색
    for i in range(N):  # 세로 N
        for j in range(M):  # 가로 M
            # 배추가 있는 곳(1)
            if field[i][j] == 1:
                worm_count += 1
                stack = [(i, j)]  # 해당 배추 위치 저장

                # 다음 배추 위치 탐색
                while stack:  # 스택에 배추 위치가 존재하는 동안
                    x, y = stack.pop()  # 해당 좌표를 꺼내와서
                    field[x][y] = 0  # 방문 처리(배추 삭제)
                    # 새로운 방향으로 이동
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 1:  # 정상 범위 내 배추가 존재하는 좌표라면
                            stack.append((nx, ny))  # 새로운 좌표를 지정

    results.append(worm_count)
    
output = "\n".join(f"{result}" for result in results)
sys.stdout.write(output + '\n')