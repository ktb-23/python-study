import sys
input = sys.stdin.read

def check_color(x, y, n):
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != color:
                return False
    return True

def divide_n(x, y, n):
    global white, blue
    if check_color(x, y, n):
        if paper[x][y] == 0:
            white += 1
        else:
            blue += 1
    else:
        half = n // 2
        divide_n(x, y, half)
        divide_n(x, y + half, half)
        divide_n(x + half, y, half)
        divide_n(x + half, y + half, half)

data = input().split()
n = int(data[0])
paper = []
index = 1

for i in range(n):
    paper.append(list(map(int, data[index:index + n])))
    index += n

white, blue = 0, 0

divide_n(0, 0, n)

print(white)
print(blue)

