import sys

# sys.stdin = open("input.txt", "r")

n = int(input())


def n_queen(row, col, sum, diff):
    if row == n:
        return 1

    ret = 0
    for j in range(0, n):
        if col[j] or sum[row + j] or diff[row - j + n]:
            continue
        col[j] = True
        sum[row + j] = True
        diff[row - j + n] = True
        ret = ret + n_queen(row + 1, col, sum, diff)
        col[j] = False
        sum[row + j] = False
        diff[row - j + n] = False
    return ret


print(n_queen(0, [False] * n, [False] * (2 * n), [False] * (2 * n)))
