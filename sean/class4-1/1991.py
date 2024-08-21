import sys

# sys.stdin = open("input.txt", "r")


def alphabet_to_number(char):
    return ord(char) - ord("A")


def number_to_alphabet(number):
    return chr(number + ord("A"))


n = int(input())
tree = [[-1, -1] for _ in range(n + 1)]

for _ in range(n):
    a, b, c = map(alphabet_to_number, input().split())
    if b != -19:  # -19 is "." (leaf node)
        tree[a][0] = b
    if c != -19:
        tree[a][1] = c


def pre_order(node):
    ret = []
    ret.append(node)
    if tree[node][0] != -1:
        ret += pre_order(tree[node][0])
    if tree[node][1] != -1:
        ret += pre_order(tree[node][1])
    return ret


def in_order(node):
    ret = []
    if tree[node][0] != -1:
        ret += in_order(tree[node][0])
    ret.append(node)
    if tree[node][1] != -1:
        ret += in_order(tree[node][1])
    return ret


def post_order(node):
    ret = []
    if tree[node][0] != -1:
        ret += post_order(tree[node][0])
    if tree[node][1] != -1:
        ret += post_order(tree[node][1])
    ret.append(node)
    return ret


print("".join(map(number_to_alphabet, pre_order(0))))
print("".join(map(number_to_alphabet, in_order(0))))
print("".join(map(number_to_alphabet, post_order(0))))
