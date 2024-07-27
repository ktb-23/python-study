n,m = map(int,input().split())
num = list(map(int,input().split()))

best = 0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            num_sum = num[i] + num[j] + num[k]
            if num_sum <= m:
                best = max(best,num_sum)
print(best)