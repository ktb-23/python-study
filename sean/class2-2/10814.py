import sys

# sys.stdin = open("input.txt", "r")

n = int(input())
lines = sys.stdin.readlines()

# sorted와 list 메서드 sort 모두 stable sort!
members = sorted(map(lambda x: x.split(), lines), key=lambda x: int(x[0]))
print("\n".join(list(map(lambda x: " ".join(x), members))))
