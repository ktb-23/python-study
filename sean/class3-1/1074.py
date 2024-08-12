import sys

# sys.stdin = open("input.txt", "r")

n, r, c = map(int, input().split())


def action(answer, size, x, y):
    if size == 1:
        return answer
    half = size // 2
    delta = half * half
    if x <= r and y <= c and x + half > r and y + half > c:
        return action(answer, half, x, y)
    elif x <= r and y + half <= c and x + half > r and y + size > c:
        return action(answer + delta, half, x, y + half)
    elif x + half <= r and y <= c and x + size > r and y + half > c:
        return action(answer + delta * 2, half, x + half, y)
    else:
        return action(answer + delta * 3, half, x + half, y + half)


print(action(0, 2**n, 0, 0))
