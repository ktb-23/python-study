import sys

# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())


def print_sequence(source, current):
    if len(source) == m:
        return print(" ".join(map(str, source)))
    if current > n:
        return

    source.append(current)
    print_sequence(source, current + 1)
    source.pop()
    print_sequence(source, current + 1)


print_sequence([], 1)
