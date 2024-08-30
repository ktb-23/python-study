import sys

input = sys.stdin.read
data = input().split()

numbers = list(map(int, data[1:]))
numbers.sort()

output = "\n".join(map(str, numbers))
sys.stdout.write(output + "\n")