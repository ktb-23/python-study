import sys

# sys.stdin = open("input.txt", "r")

n, k = map(int, input().split())
queue = [x for x in range(1, n + 1)]

answer = []

cursor = k - 1
while len(queue) is not 0:
    if cursor >= len(queue):
        cursor = cursor % len(queue)
    answer.append(queue[cursor])
    queue.pop(cursor)
    cursor = cursor + k - 1

print(f'<{", ".join(map(str, answer))}>')
