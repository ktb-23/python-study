import sys

# n을 2x1, 1x2 타일로 채우는 방법의 수 계산
memo = {1: 1, 2: 2}

def calculate_ways(n):

    # n이 1, 2인 경우    
    if n in memo:
        return memo[n]

    # n이 3 이상인 경우
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2] % 10007  # 메모리를 위해 미리 나머지 계산
    return memo[n]


# 입력 처리
input = sys.stdin.read
data = input().strip()

# 첫째 줄: 2*n에서의 숫자 n
n = int(data)

# 결과값
result = calculate_ways(n) % 10007

# 출력 결과
sys.stdout.write(str(result) + '\n')