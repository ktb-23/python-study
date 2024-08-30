A, B, C = map(int,open(0).read().split())

result = 1  # A**0 = 항상 1
for _ in range(B):
    result = result * A % C
print(result)