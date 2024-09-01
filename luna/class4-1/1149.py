num_house, *costs = map(int,open(0).read().split())   # num_house = 3, costs = [26, 40, 83, 49, 60, 57, 13, 89, 99]

for i in range(3, len(costs)):  # cost의 인덱스는 0부터 시작
    if i == 3:
        costs[i] += min(costs[1], costs[2])
    elif i % 3 == 0:
        costs[i] += min(costs[i-1], costs[i-2])
    elif i % 3 == 1:
        costs[i] += min(costs[i-2], costs[i-4])
    else:
        costs[i] += min(costs[i-4], costs[i-5])
    
print(min(costs[-1],costs[-2],costs[-3]))