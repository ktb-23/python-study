n = int(input())
member = []

for i in range(n):
    age, name = input().split() 
    age = int(age)
    member.append((age, name))
    
member.sort(key=lambda x: x[0])

for age, name in member:
    print(age,name)
    