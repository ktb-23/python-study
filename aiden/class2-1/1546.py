n = int(input())
scores = list(map(int,input().split()))
m = max(scores)

after_score = [(score/ m) * 100 for score in scores]
after_mean = sum(after_score) / n

print(f"{after_mean}")