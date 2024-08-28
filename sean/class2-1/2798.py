from functools import reduce
import sys

# sys.stdin = open("input.txt", "r")


n, m = map(int, input().split())
cards = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(n):
        if i is j:
            continue
        for k in range(n):
            if i is k or j is k:
                continue
            candidate = sum([cards[i], cards[j], cards[k]])
            ans = max(ans, candidate) if candidate <= m else ans

print(ans)
