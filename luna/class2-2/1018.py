import sys

input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
chess_board = data[1:]

min_repaints = 64
    
for i in range(n - 7):
    for j in range(m - 7):
        repaints_W = 0
        repaints_B = 0

        for x in range(8):
            for y in range(8):
                white = 'W' if (x + y) %2 == 0 else 'B'
                black = 'B' if (x + y) %2 == 0 else 'W'

                if chess_board[i + x][j + y] != white:
                    repaints_W += 1
                if chess_board[i + x][j + y] != black:
                    repaints_B += 1

        min_repaints = min(min_repaints, repaints_W, repaints_B)

sys.stdout.write(str(min_repaints) + '\n')