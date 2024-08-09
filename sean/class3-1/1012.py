from collections import deque
import sys

# sys.stdin = open("input.txt", "r")

t = int(input())


def count_required_bug(n, m, k):
    farm = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        farm[x][y] = 1

    ret = 0
    mx = [0, 0, 1, -1]
    my = [1, -1, 0, 0]
    flag = [[0 for _ in range(m)] for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if flag[x][y] or farm[x][y] == 0:
                continue
            flag[x][y] = True
            ret += 1
            que = deque()
            que.append((x, y))
            while que:
                cur_x, cur_y = que.popleft()
                for i in range(len(mx)):
                    next_x = cur_x + mx[i]
                    next_y = cur_y + my[i]
                    if (
                        next_x < 0
                        or next_y < 0
                        or next_x >= n
                        or next_y >= m
                        or farm[next_x][next_y] == 0
                        or flag[next_x][next_y]
                    ):
                        continue
                    flag[next_x][next_y] = True
                    que.append((next_x, next_y))
    return ret


for _ in range(t):
    print(count_required_bug(*list(map(int, input().split()))))
