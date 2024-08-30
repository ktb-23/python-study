import sys


input = sys.stdin.read

data = input().split()
n, m = int(data[0]), int(data[1])
board = data[2:]
change = float('inf')

for i in range(n - 7):      
    for j in range(m - 7):
        change_black = 0
        change_white = 0
        
        for x in range(8):
            for y in range(8):
                black = 'B' if ( x + y ) % 2 == 0 else 'W'
                white = 'W' if ( x + y ) % 2 == 0 else 'B'
                if board[i+y][j+x] != black:
                    change_black += 1
                if board[i+y][j+x] != white:
                    change_white += 1
        
        change = min(change,change_black,change_white)
        
print(change)