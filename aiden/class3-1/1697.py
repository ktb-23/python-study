from collections import deque

def walk(x):
    return [x-1,x+1]

def tel(x):
    return x * 2

def bfs(n,k):
    max_limit = 100001
    visit = [False] * max_limit
    distance = [0] * max_limit

    queue = deque([n])
    visit[n] = True

    while queue:
        current = queue.popleft()

        if current == k:
            return distance[current]  

        for next_pos in walk(current):
            if 0 <= next_pos < max_limit and not visit[next_pos]:
                visit[next_pos] = True
                distance[next_pos] = distance[current] + 1
                queue.append(next_pos)

        next_pos = tel(current)
        if 0 <= next_pos < max_limit and not visit[next_pos]:
            visit[next_pos] = True
            distance[next_pos] = distance[current] + 1
            queue.append(next_pos)

n, k = map(int, input().split())
print(bfs(n, k))