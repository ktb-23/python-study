import sys
from itertools import permutations

def generate_permutations(numbers, m):
    # n개의 수(=numbers) 중에서 m개를 선택하는 순열(p) 생성
    return sorted(permutations(numbers, m))

# 입력 처리
input = sys.stdin.read
data = input().strip().splitlines()

# 첫째 줄: 자연수 N, M (1 <= M <= N <= 8)
N, M = map(int, data[0].split())
# 둘째 줄: N개의 수 (x <= 10,000)
nums = list(map(int, data[1].split()))

# 출력 결과
output = '\n'.join(' '.join(map(str, perm)) for perm in generate_permutations(nums, M))
sys.stdout.write(output + '\n')