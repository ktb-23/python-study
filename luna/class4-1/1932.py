import sys

def max_sum_triangle(triangle, n):
    for i in range(n-2, -1, -1):  # 아래에서 위로 역순으로 이동, i의 범위는 n-1 ~ 0
        for j in range(i+1):  # j의 범위는 i의 x 좌표의 +0 ~ +1
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])  # 아래 두 값 중 더 큰 값을 더함
            
    return triangle[0][0]  # 최종적으로 가장 위에 최대 합이 남음

# 입력 처리
input = sys.stdin.read
data = input().strip().splitlines()

# 첫째 줄: 삼각형의 크기
n = int(data[0])

# 다음 n줄: 정수 삼각형의 정보 (각 줄의 값들, 공백 구분)
triangle = [list(map(int, line.split())) for line in data[1:]]

# 출력 결과
output = str(max_sum_triangle(triangle, n))
sys.stdout.write(output + '\n')