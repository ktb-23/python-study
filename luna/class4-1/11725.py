from collections import deque

N, *edges = map(int, open(0).read().split())  # edges = [1, 6, 6, 3, ...]
tree = [[] for _ in range(N + 1)]

for a, b in zip(edges[::2], edges[1::2]):  # 2씩 건너뛰며 zip [1, 6], [6, 3], ...
    tree[a] += [b]  # 연결된 노드 리스트 저장
    tree[b] += [a]

parents = [0] * (N + 1)
queue = deque([1])

while queue:
    current = queue.popleft()
    for next_node in tree[current]:
        if not parents[next_node]:
            parents[next_node] = current
            queue.append(next_node)

print('\n'.join(map(str, parents[2:])))  # 2번 노드부터 출력