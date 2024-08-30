N, *data = [*open(0)]
lines = [list(map(int, _.split())) for _ in data]

for i in range(int(N)):
    num = lines[3*i][0]
    top_row = lines[3*i + 1]
    bottom_row = lines[3*i + 2]
    
    if num > 1:
        top_row[1] += bottom_row[0]
        bottom_row[1] += top_row[0]
        
    for j in range(2, num):
        top_row[j] += max(bottom_row[j-1], bottom_row[j-2])
        bottom_row[j] += max(top_row[j-1], top_row[j-2])

    print(max(top_row[-1], bottom_row[-1]))