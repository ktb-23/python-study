t = int(input())

count_zero = [1, 0] + [0] * 39
count_one = [0, 1] + [0] * 39

for i in range(2, 41):
    count_zero[i] = count_zero[i-1] + count_zero[i-2]
    count_one[i] = count_one[i-1] + count_one[i-2]

for _ in range(t):
    n = int(input())
    print(count_zero[n], count_one[n])   
