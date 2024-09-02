import heapq
import sys

# sys.stdin = open("input.txt", "r")

v, e = map(int, input().split())
k = int(input())


graph = {i: [] for i in range(1, v + 1)}
for i in range(e):
    _u, _v, _w = map(int, input().split())
    graph[_u].append((_v, _w))

distance = [float("inf")] * (v + 1)
distance[k] = 0

pq = []
heapq.heappush(pq, (0, k))

while pq:
    _w, cur = heapq.heappop(pq)

    if _w > distance[cur]:
        continue

    for next, weight in graph[cur]:
        next_weight = _w + weight
        if next_weight < distance[next]:
            distance[next] = next_weight
            heapq.heappush(pq, (next_weight, next))

print("\n".join(map(lambda x: str(x) if x != float("inf") else "INF", distance[1:])))
