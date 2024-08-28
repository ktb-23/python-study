from math import comb

n, k = map(int, input().split())

binomial = comb(n, k)

print(binomial)