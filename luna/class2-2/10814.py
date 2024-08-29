import sys

input = sys.stdin.read
data = input().splitlines()

members = []

for i in range(1, int(data[0])+1):
    age, name = data[i].split()
    members.append((int(i), int(age), name))

members.sort(key=lambda x: (x[1], x[0]))

output = "\n".join(f"{age} {name}" for _, age, name in members)
sys.stdout.write(output + "\n")