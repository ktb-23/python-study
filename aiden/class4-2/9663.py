def safe(row, col):
    for i in range(row):
        if col == queens[i] or abs(col - queens[i]) == row - i:
            return False
    return True

def near_queens(row):
    global count # 전역 변수 count를 사용하겠다는 선언
    # 사용 시 def 함수 외에서 선언된 변수를 내부에서 사용 가능
    if row == n:
        count += 1
        return
    for col in range(n):
        if not col_used[col] and not diag1_used[row + col] and not diag2_used[row - col + n - 1]:
            col_used[col] = diag1_used[row + col] = diag2_used[row - col + n - 1] = True
            near_queens(row + 1)
            col_used[col] = diag1_used[row + col] = diag2_used[row - col + n - 1] = False

n = int(input())
col_used = [False] * n
diag1_used = [False] * (2 * n - 1)
diag2_used = [False] * (2 * n - 1)
count = 0
near_queens(0)
print(count)
