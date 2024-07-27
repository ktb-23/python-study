t = int(input())

for i in range(t):
    r,s = input().split()
    r = int(r)
    answer = ''
    for char in s:
        answer += char * r
        print(answer)
