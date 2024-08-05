import sys

# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())

board = []

right_board_1 = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
]

right_board_2 = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
]

for i in range(n):
    board.append(input())

# 최대 연산 횟수는 50 * 50 * 64
answer = n * m + 1
for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        candiate_1 = 0
        candiate_2 = 0

        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if board[x][y] is not right_board_1[x - i][y - j]:
                    candiate_1 = candiate_1 + 1
                if board[x][y] is not right_board_2[x - i][y - j]:
                    candiate_2 = candiate_2 + 1

        answer = min(answer, candiate_1, candiate_2)

print(answer)
