import sys
input = sys.stdin.read


data = input().strip().split()


n = int(data[0])
point = []
index = 1


for i in range(n):
    x = int(data[index])
    y = int(data[index + 1])
    point.append((x, y))
    index += 2


point.sort()


for x, y in point:
    print(x, y)
