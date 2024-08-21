import sys
from collections import deque


def count_infected_computers(n, connections):
    # n개의 그래프 초기화
    graph = [[] for _ in range(n + 1)]
    
    # 연결 정보를 그래프로 저장
    for x, y in connections:
        graph[x].append(y)
        graph[y].append(x)
    
    # 방문했는지 체크하기 위한 배열
    visited = [False] * (n + 1)
    
    # 1번 컴퓨터에서부터 시작
    queue = deque([1])
    visited[1] = True
    infected_count = 0

    # queue가 비어있지 않은 동안 탐색
    while queue:
        node = queue.popleft()
        
        # 현재 노드와 연결된 모든 노드를 탐색
        for neighbor in graph[node]:
            if not visited[neighbor]:  # False라면
                visited[neighbor] = True  # True로 바꾸고
                queue.append(neighbor)  # queue에 해당 컴퓨터 추가
                infected_count += 1  # 감염된 컴퓨터 +1
        
    return infected_count  # 감염된 컴퓨터 수 반환
        

# 입력 처리
input = sys.stdin.read
data = input().strip().splitlines()

# 첫째 줄: 컴퓨터의 수(100 이하인 양의 정수)
n = int(data[0])

# 둘째 줄: 네트워크 상에서 직접 연결된 컴퓨터 쌍의 수
m = int(data[1])

# 다음 m줄: 네트워크 연결 정보(컴퓨터의 번호 쌍)
connections = [tuple(map(int, line.strip().split())) for line in data[2:m+2]]

# 출력 결과
output = str(count_infected_computers(n, connections))
sys.stdout.write(output + '\n')