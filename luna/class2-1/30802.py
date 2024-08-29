participants = int(input())
sizes = list(map(int,input().split()))
t, p = map(int,input().split())
Tset = 0
for size in sizes:
    Tset += size // t
    if size % t:
        Tset += 1
Pset = participants // p
remaining = participants % p
print(Tset)
print(Pset, remaining)