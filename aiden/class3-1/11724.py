import sys
sys.setrecursionlimit(10000) # 10000까지 제한

input = sys.stdin.read
data = input().split()

def dfs(node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)

n, m = map(int, data[0:2])
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

index = 2
for _ in range(m):
    u, v = map(int, data[index : index + 2])
    graph[u].append(v)
    graph[v].append(u)
    index += 2

count = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)