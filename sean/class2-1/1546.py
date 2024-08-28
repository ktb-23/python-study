import sys

# sys.stdin = open("input.txt", "r")

n = int(input())
real_scores = list(map(int, input().split()))
max_score = max(real_scores)

average = sum(map(lambda x: x/max_score*100, real_scores))/n
print(average)