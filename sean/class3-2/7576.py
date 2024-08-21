from collections import deque
import sys

# sys.stdin = open("input.txt", "r")

m, n = map(int, input().split())

box_info = []
que = deque()

unriped = 0
for i in range(n):
    row = list(map(int, input().split()))
    box_info.append(row)
    for j in range(m):
        if row[j] == 1:
            que.append((i, j))
        elif row[j] == 0:
            unriped += 1

mx = [0, 0, 1, -1]
my = [1, -1, 0, 0]

answer = 1
while que:
    cur_x, cur_y = que.popleft()
    cur_day = box_info[cur_x][cur_y]
    for i in range(4):
        next_x = cur_x + mx[i]
        next_y = cur_y + my[i]
        if (
            next_x < 0
            or next_x >= n
            or next_y < 0
            or next_y >= m
            or box_info[next_x][next_y] == -1
            or box_info[next_x][next_y] > 0
        ):
            continue
        unriped -= 1
        box_info[next_x][next_y] = cur_day + 1
        answer = max(cur_day + 1, answer)
        que.append((next_x, next_y))

print(-1 if unriped > 0 else answer - 1)
