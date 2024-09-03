import sys
from collections import deque, defaultdict

data = sys.stdin.read().split()

n = int(data[0])
index = 1
graph = defaultdict(list)

for _ in range(n-1):
    u, v, w = map(int, data[index:index+3])
    graph[u].append((v, w))
    graph[v].append((u, w))
    index += 3

def bfs(start):
    distance = [-1] * (n + 1)
    distance[start] = 0
    q = deque([start])

    max_dist = 0
    farthest_node = start

    while q:
        node = q.popleft()

        for neighbor, weight in graph[node]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[node] + weight
                q.append(neighbor)

                if distance[neighbor] > max_dist:
                    max_dist = distance[neighbor]
                    farthest_node = neighbor

    return farthest_node, max_dist

farthest_node, _ = bfs(1)

_, tree_diameter = bfs(farthest_node)

print(tree_diameter)
