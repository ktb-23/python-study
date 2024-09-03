import sys
import heapq

data = sys.stdin.read().split()
inf = int(1e9)

V = int(data[0])
E = int(data[1]) 
K = int(data[2]) 

graph = [[] for _ in range(V + 1)]
distance = [inf] * (V + 1)

index = 3

for _ in range(E):
    u = int(data[index])
    v = int(data[index + 1])
    w = int(data[index + 2])
    graph[u].append((v, w))
    index += 3

def short_distance(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

short_distance(K)

for i in range(1, V + 1):
    if distance[i] == inf:
        print("INF")
    else:
        print(distance[i])
