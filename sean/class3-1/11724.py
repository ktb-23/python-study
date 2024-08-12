from collections import deque
import sys

# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())

connections = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    connections[u].append(v)
    connections[v].append(u)

flag = [False] * (n + 1)

answer = 0
for i in range(1, n + 1):
    if flag[i]:
        continue
    flag[i] = True
    answer += 1
    que = deque([i])
    while que:
        current = que.popleft()
        for next in connections[current]:
            if flag[next]:
                continue
            flag[next] = True
            que.append(next)

print(answer)
