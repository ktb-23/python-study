import heapq
import sys

# sys.stdin = open("input.txt", "r")

minheap = []

data = list(map(int, sys.stdin.read().splitlines()))

n = data[0]
for x in data[1:]:
    if x == 0:
        print(heapq.heappop(minheap) if minheap else 0)
    else:
        heapq.heappush(minheap, x)
