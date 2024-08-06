import sys

# sys.stdin = open("input.txt", "r")

n = int(input())
word = set()
for _ in range(n):
    word.add(input())

sorted_word = sorted(word, key=lambda word: (len(word), word))
# sorted_word = sorted(word, key=lambda word: len(word)) # 해당 방식은 문자열 정렬이 이루어지지 않아서 실패 함

print("\n".join(sorted_word))
