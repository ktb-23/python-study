import sys

# sys.stdin = open("input.txt", "r")

memo = [[-1, -1] for _ in range(41)]
memo[0] = [1, 0]
memo[1] = [0, 1]


def fibonacci(n):
    if memo[n][0] is not -1:
        return memo[n]

    # list(map(lambda x, y: x + y, list1, list2)) 과 동일
    memo[n] = [x + y for x, y in zip(fibonacci(n - 1), fibonacci(n - 2))]

    return memo[n]


t = int(input())
for _ in range(t):
    n = int(input())
    print(" ".join(map(str, fibonacci(n))))
