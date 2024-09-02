import sys

# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

sum_arr = [[0] * n for _ in range(n)]

for i in range(0, n):
    for j in range(n):
        prev_row = sum_arr[i - 1][j] if (i != 0) else 0
        prev_col = sum_arr[i][j - 1] if (j != 0) else 0
        prev_sum = sum_arr[i - 1][j - 1] if (i != 0 and j != 0) else 0
        sum_arr[i][j] = arr[i][j] + prev_row + prev_col - prev_sum

for _ in range(m):
    x1, y1, x2, y2 = map(lambda x: int(x) - 1, input().split())
    prev_row = sum_arr[x1 - 1][y2] if (x1 != 0) else 0
    prev_col = sum_arr[x2][y1 - 1] if (y1 != 0) else 0
    prev_sum = sum_arr[x1 - 1][y1 - 1] if (x1 != 0 and y1 != 0) else 0
    print(sum_arr[x2][y2] - prev_row - prev_col + prev_sum)
