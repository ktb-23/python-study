import sys
sys.setrecursionlimit(10**6)

def find_connected_component(n, lines):
    graph = [[] for _ in range(n + 1)]
    
    # 간선 정보를 바탕으로 그래프 구축
    # 방향 없는 그래프이므로 양쪽 노드 모두 추가
    for u, v in lines:
        graph[u].append(v)
        graph[v].append(u)
        
    # 방문 여부를 기록하는 리스트
    visited = [False] * (n + 1)
    
    # 깊이 우선 탐색
    def dfs(node):
        # 현재 노드를 방문 처리
        visited[node] = True
        # 인접 노드들에 대해 탐색
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)

        
    # 연결 요소 계산
    count = 0

    for node in range(1, n + 1):
        if not visited[node]:
            count += 1
            dfs(node)
            
    return count

# 입력 처리
input = sys.stdin.read
data = input().strip().splitlines()

# 첫째 줄: 정점의 개수 N, 간선의 개수 M
N, M = map(int, data[0].split())
# 다음 M줄: 연결 정보(간선의 양 끝점 u, v)
connections = [tuple(map(int, line.strip().split())) for line in data[1:M+1]]

# 출력 결과
output = str(find_connected_component(N, connections))
sys.stdout.write(output + '\n')