from collections import deque
import sys

# sys.stdin = open("input.txt", "r")

computer_count = int(input())
pair_count = int(input())

# network = [[]] * (computer_count + 1)는 []를 공유해서 안됨
# *는 내부 메모리에 있는 값을 복제하는 방식
network = [[] for _ in range(computer_count + 1)]
for _ in range(pair_count):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

flag = [False] * (computer_count + 1)
pathways = deque([1])
flag[1] = True
while pathways:
    current = pathways.popleft()
    for next in network[current]:
        if flag[next]:
            continue
        flag[next] = True
        pathways.append(next)

print(len(list(filter(lambda x: x, flag))) - 1)
