import sys
from collections import Counter

input = sys.stdin.read
data = input().splitlines()

cards = list(map(int, data[1].split()))
targets = list(map(int, data[3].split()))

card_counter = Counter(cards)

count = [card_counter[target] for target in targets]

output = " ".join(map(str, count))
sys.stdout.write(output + '\n')