import sys
from collections import deque, defaultdict

data = sys.stdin.read().split()
n = int(data[0])

graph = defaultdict(list)
index = 1
# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.
for i in range(n - 1):
    a = int(data[index])
    b = int(data[index+1])
    graph[a].append(b)
    graph[b].append(a)
    index += 2

parent = [0] * (n + 1)

def bfs():
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if parent[neighbor] == 0:
                parent[neighbor] = node
                queue.append(neighbor)

bfs()

for i in range(2, n + 1):
    print(parent[i])