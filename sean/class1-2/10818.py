import sys

# sys.stdin = open("input.txt", "r")

n = int(input())

#NOTE: map은 Map class의 인스턴스(object)를 반환하므로 변환 해주어야 함
sequence = list(map(int, input().split()))

#NOTE: min, max는 iterable만 사용 가능
print(f'{min(sequence)} {max(sequence)}')