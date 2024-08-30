import sys

input = sys.stdin.read
data = input().splitlines()

points = []

for i in range(1, int(data[0])+1):
    x, y = data[i].split()
    points.append((int(x), int(y)))

points.sort()

output = "\n".join(f"{x} {y}" for x, y in points)
sys.stdout.write(output + "\n")