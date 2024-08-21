from collections import deque
import sys

# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())

load_map = []
my_map = [[-1 for _ in range(m)] for _ in range(n)]

target_x = -1
target_y = -1
for i in range(n):
    load_map.append(list(map(int, input().split())))
    for j in range(m):
        if load_map[i][j] == 2:
            target_x = i
            target_y = j
        elif load_map[i][j] == 0:
            my_map[i][j] = 0

que = deque([(target_x, target_y)])

my_map[target_x][target_y] = 0

mx = [0, 0, 1, -1]
my = [1, -1, 0, 0]

while que:
    cur_x, cur_y = que.popleft()
    cur_distance = my_map[cur_x][cur_y]
    for i in range(4):
        next_x = cur_x + mx[i]
        next_y = cur_y + my[i]
        if (
            next_x < 0
            or next_x >= n
            or next_y < 0
            or next_y >= m
            or load_map[next_x][next_y] == 0
            or my_map[next_x][next_y] > -1
        ):
            continue
        my_map[next_x][next_y] = cur_distance + 1
        que.append((next_x, next_y))

for row in my_map:
    print(" ".join(map(str, row)))
