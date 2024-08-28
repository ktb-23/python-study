import sys


from collections import deque

input = sys.stdin.read

n = int(input().strip())  
cards = deque(range(1, n + 1))

while len(cards) > 1:
    cards.popleft()  
    cards.rotate(-1)  

print(cards.pop())