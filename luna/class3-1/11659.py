import sys

# 입력 처리
input = sys.stdin.read
data = input().strip().splitlines()

# 첫째 줄: 수의 개수 N, 합을 구해야 하는 횟수 M
N, M = map(int, data[0].split())

# 둘째 줄: N개의 수
numbers = list(map(int, data[1].split()))

# 다음 m줄: 합을 구해야 하는 구간 i와 j
intervals = [tuple(map(int, line.strip().split())) for line in data[2:M+2]]

# 출력해야 하는 결과값 저장 리스트
results = []


# 누적 합 계산 방법
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + numbers[i - 1]

# 구간 합 계산 방법
for i, j in intervals:
    result = prefix_sum[j] - prefix_sum[i - 1]
    results.append(result)


# 출력 결과
output = "\n".join(map(str, results))
sys.stdout.write(output + '\n')