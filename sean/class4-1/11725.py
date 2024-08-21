from collections import deque
import sys

# sys.stdin = open("input.txt", "r")

n = int(input())

tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

flag = [False] * (n + 1)
que = deque([1])
flag[1] = True

parent = [0] * (n + 1)

while que:
    node = que.popleft()
    for i in tree[node]:
        if flag[i]:
            continue
        parent[i] = node
        flag[i] = True
        que.append(i)

print("\n".join(map(str, parent[2:])))
