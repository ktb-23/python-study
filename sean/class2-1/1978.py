from functools import reduce
import sys

# sys.stdin = open("input.txt", "r")


def is_multiple_of_source_numbers(target, source_numbers):
    for source in source_numbers:
        if target % source == 0:
            return True
    return False


n = int(input())
prime_numbers = reduce(
    lambda acc, cur: (
        acc + [cur] if not is_multiple_of_source_numbers(cur, acc) else acc
    ),
    range(3, 1001),
    [2],
)

print(sum(1 for num in list(map(int, input().split())) if num in prime_numbers))
