from collections import deque
import sys

# sys.stdin = open("input.txt", "r")

n = int(input())

tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

answer = 0
for root in range(1, n + 1):
    visited = [-1] * (n + 1)
    visited[root] = 0

    queue = deque([root])
    while queue:
        cur = queue.popleft()

        for next, weight in tree[cur]:
            if visited[next] == -1:
                visited[next] = visited[cur] + weight
                queue.append(next)
                answer = max(answer, visited[next])

print(answer)
