import sys

# sys.stdin = open("input.txt", "r")


def is_right_triangle(a, b, c):
    return (
        pow(a, 2) + pow(b, 2) == pow(c, 2)
        or pow(b, 2) + pow(c, 2) == pow(a, 2)
        or pow(c, 2) + pow(a, 2) == pow(b, 2)
    )


lines = sys.stdin.readlines()
for line in lines:
    a, b, c = map(int, line.split())
    if a == 0 and b == 0 and c == 0:
        break
    if is_right_triangle(a, b, c):
        print("right")
    else:
        print("wrong")
