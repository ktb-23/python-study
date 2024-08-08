import sys

# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())

name_list = sys.stdin.read().splitlines()

# python set은 hash를 사용하여 관리하므로 순서를 보장하지 않음
not_listened = set(name_list[:n])
not_met = set(name_list[n:])

answer = not_listened.intersection(not_met)
print(len(answer))
print("\n".join(sorted(answer)))
