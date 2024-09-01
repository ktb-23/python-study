from itertools import permutations

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

sequences = permutations(numbers, m)

for sequence in sequences:
    print(' '.join(map(str, sequence)))

