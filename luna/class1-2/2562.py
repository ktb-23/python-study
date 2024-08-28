num = []

for i in range(9):
    n = int(input())
    num.append(n)

print(max(num))
print(num.index(max(num))+1)