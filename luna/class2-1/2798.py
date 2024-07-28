from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

cards_set = [sum(set) for set in combinations(cards, 3)]
result = max(i for i in cards_set if i <= m)

print(result)