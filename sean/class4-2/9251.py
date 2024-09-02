import sys

# sys.stdin = open("input.txt", "r")

sequence = [input(), input()]

sequence_table = [[0] * (len(sequence[1]) + 1) for _ in range(len(sequence[0]) + 1)]


answer = 0
for i in range(1, len(sequence[0]) + 1):
    for j in range(1, len(sequence[1]) + 1):
        if sequence[0][i - 1] == sequence[1][j - 1]:
            prev = sequence_table[i - 1][j - 1] if (i != 0 and j != 0) else 0
            sequence_table[i][j] = prev + 1
        else:
            prev_row = sequence_table[i - 1][j] if (i != 0) else 0
            prev_col = sequence_table[i][j - 1] if (j != 0) else 0
            sequence_table[i][j] = max(prev_row, prev_col)
        answer = max(answer, sequence_table[i][j])

print(answer)