import sys

# memory
# 0: 1개 (-)
# 1: 1개 (1)
# 2: 2개 (11 2)
# 3: 4개 (111 12 21 3)
memo = {0: 1, 1: 1, 2: 2, 3: 4}

def calculate_ways(n):
    if n in memo:
        return memo[n]
    memo[n] = calculate_ways(n-1) + calculate_ways(n-2) + calculate_ways(n-3)
    return memo[n]


# 입력 처리
input = sys.stdin.read
data = input().strip().splitlines()

# 첫째 줄: 테스트 케이스 개수
t = int(data[0])

# 각 테스트 케이스에 대한 결과를 저장할 리스트
results = []

# 다음 t줄: 각각의 테스트 케이스 n
for line in data[1:t+1]:
    n = int(line.strip())
    # 각 n에 대해 함수 결과를 저장
    result = calculate_ways(n)
    results.append(result)

# 출력 결과
output = "\n".join(map(str, results))
sys.stdout.write(output + '\n')