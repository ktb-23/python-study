import heapq
import sys

# sys.stdin = open("input.txt", "r")

n = int(input())

numbers = list(map(int, input().split()))

unique_numbers = set(sorted(numbers))

minheap = []

for number in unique_numbers:
    heapq.heappush(minheap, -number)

answer_dict = {}
while minheap:
    current = heapq.heappop(minheap)
    answer_dict[-current] = len(minheap)

for number in numbers:
    print(answer_dict[number], end=" ")
