import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
x_list = list(map(int, data[1:n + 1]))

sorted_x_list = sorted(set(x_list))
x_list_dict = {value: index for index, value in enumerate(sorted_x_list)}
compressed_x_list = [x_list_dict[value] for value in x_list]

print(' '.join(map(str, compressed_x_list)))