n = int(input())
size = list(map(int,input().split()))
t,p = map(int,input().split())

answer = 0

for i in range(len(size)):
    if size[i] % t == 0:
        answer += int(size[i]/t)
    else:
        answer += (int(size[i]/t)+1)

answer2 = [int(sum(size)/p),sum(size)%p]

print(answer)
print(*answer2)