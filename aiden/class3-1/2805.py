import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
h = list(map(int, data[2:]))

start = 0
end = max(h)

answer = 0
while start <=end:
    mid = (start + end) // 2
    total = 0
    
    for trees in h:
        if trees > mid:
            total += trees - mid
    
    if total >= m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
