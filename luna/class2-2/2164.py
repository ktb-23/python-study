import sys
from collections import deque

num = int(sys.stdin.read().strip())

card_list = deque(range(1, num + 1))

while len(card_list) > 1:
    card_list.popleft()
    card_list.append(card_list.popleft())

sys.stdout.write(str(card_list[0]) + '\n')