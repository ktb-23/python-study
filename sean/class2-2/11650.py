import sys

# sys.stdin = open("input.txt", "r")

n = int(input())
coordinate = []

for _ in range(n):
    coordinate.append(list(map(int, input().split())))

sorted_coordinate = sorted(coordinate)
for i in range(len(sorted_coordinate)):
    print(f"{sorted_coordinate[i][0]} {sorted_coordinate[i][1]}")
