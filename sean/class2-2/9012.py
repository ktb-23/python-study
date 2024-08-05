import sys

# sys.stdin = open("input.txt", "r")

t = int(input())

for _ in range(t):
    text = input()
    stack = []
    for c in text:
        if c == "(":
            stack.append("(")
        else:
            if len(stack) == 0:
                stack.append("(")
                break
            stack.pop()

    print("YES" if len(stack) == 0 else "NO")
