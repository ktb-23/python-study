import sys


input = sys.stdin.read
data = input().strip().split()

n = int(data[0])
words = data[1:]

words = list(set(words))
words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)
