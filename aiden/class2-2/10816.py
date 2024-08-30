import sys


input = sys.stdin.read

data = input().split()

n = int(data[0])
cards = list(map(int, data[1:n + 1]))

m = int(data[n + 1])
targets = list(map(int, data[n + 2:]))

card_count = {}
for card in cards:
    if card in card_count:
        card_count[card] += 1
    else:
        card_count[card] = 1

result = []
for target in targets:
    if target in card_count:
        result.append(card_count[target])
    else:
        result.append(0)

print(' '.join(map(str, result)))
