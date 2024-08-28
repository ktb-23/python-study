import sys

# sys.stdin = open("input.txt", "r")

n = int(input())
s_card_list = map(int, input().split())
s_card_count = dict()

for num in s_card_list:
    if num in s_card_count:
        s_card_count[num] = s_card_count[num] + 1
    else:
        s_card_count[num] = 1

m = int(input())
targets = map(int, input().split())

for num in targets:
    print(s_card_count.get(num, 0), end=" ")
