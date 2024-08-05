# import queue를 사용하는 경우 런타임 에러 발생.
# 추가로 queue.Queue()는 멀티쓰레드 환경을 지원하기 위해 사용하는것으로
# deque보다 느림
import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

n = int(input())
deck = deque()

for i in range(1, n + 1):
    deck.append(i)

while len(deck) > 1:
    deck.popleft()
    deck.append(deck.popleft())

print(deck.popleft())
