import sys

# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
source = sorted(list(map(int, input().split())))


def print_sequence(target, flag):
    if len(target) == m:
        return print(" ".join(map(str, target)))

    for current in range(n):
        if flag[current]:
            continue

        target.append(source[current])
        flag[current] = True
        print_sequence(target, flag)
        target.pop()
        flag[current] = False


print_sequence([], [False] * n)
