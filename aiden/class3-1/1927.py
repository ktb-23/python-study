import sys
import heapq

input = sys.stdin.read
data = input().split()

n = int(data[0])
heap = []
result = []

for i in range(1, n+1):
    x = int(data[i])
    if x == 0:
        if heap:
            result.append(str(heapq.heappop(heap)))
        else:
            result.append('0')
    else:
        heapq.heappush(heap, x)

sys.stdout.write("\n".join(result) + "\n")
