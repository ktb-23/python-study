import sys

def largest_A(n, A_s):
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if A_s[j] < A_s[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# 입력 처리
input = sys.stdin.read
data = input().strip().splitlines()

# 첫째 줄: 수열의 크기
n = int(data[0])

# 둘째 줄: 수열을 이루고 있는 N개의 A_i들
A_s = list(map(int, data[1].split()))

# 출력 결과
output = str(largest_A(n, A_s))
sys.stdout.write(output + '\n')