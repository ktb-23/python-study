import sys
from itertools import combinations

def generate_combinations(n, m):
    # 1부터 n까지의 수 중에서 m개를 선택하는 조합(c) 생성
    return combinations(range(1, n+1), m)

# 입력 처리
input = sys.stdin.read
data = input().strip().splitlines()

# 첫째 줄: 자연수 N, M
N, M = map(int, data[0].split())

# 출력 결과
output = '\n'.join(' '.join(map(str, combo)) for combo in generate_combinations(N, M))
sys.stdout.write(output + '\n')