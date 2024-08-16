n = int(input())
time = list(map(int,input().split()))
# 1번 사람 시간 p1 , n번 사람 p1+...pn > 시간 작은 사람이 먼저 출금
time.sort()

total = 0
cumsum = 0

for i in time:
    cumsum += i
    total += cumsum

print(total)
