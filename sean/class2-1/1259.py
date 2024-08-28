import sys

# sys.stdin = open("input.txt", "r")

# is는 동일 객체 여부 파악, ==는 동일 값 여부 파악

while True:
  number = input()
  if number == '0':
    break
  if number == number[::-1]:
    print('yes')
  else:
    print('no')