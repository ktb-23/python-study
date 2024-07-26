n1, n2 = map(int, input().split())
a, b = n1, n2

while n2 != 0:
    n1, n2 = n2, n1 % n2
    
gcd = n1
lcm = (a * b) // gcd

print(gcd)
print(lcm)