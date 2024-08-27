from itertools import combinations

n, m = map(int,input().split())

sequences = combinations(range(1, n + 1), m)
for sequence in sequences:
    print(' '.join(map(str, sequence)))
    