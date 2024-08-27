import sys

# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

flag = {}
for i in nums:
    if i in flag:
        flag[i]["count"] += 1
        continue
    flag[i] = {"count": 1, "index": len(flag)}

source = [[v, d["count"]] for v, d in flag.items()]


def action(target: list, flag):
    if len(target) == m:
        return print(" ".join(map(str, target)))

    for current in range(len(source)):
        if flag[current] >= source[current][1]:
            continue

        target.append(source[current][0])
        flag[current] += 1
        action(target, flag)
        target.pop()
        flag[current] -= 1


action([], [0] * len(source))
