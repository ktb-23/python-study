import sys

input = sys.stdin.read
data = int(input().strip())

def min_operation(x):
    # dp[x]는 숫자 x를 1로 만들기 위한 최소 연산 횟수
    # dp를 x+1개 생성 (0번 ~ x번)
    dp = [0] * (x + 1)

    for i in range(2, x + 1):
        # 1을 빼는 연산
        dp[i] = dp[i - 1] + 1
        
        # 2로 나누어 떨어지는 경우
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        
        # 3으로 나누어 떨어지는 경우
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    # 최종값(x에 대한 최소 연산 횟수) 반환
    return dp[x]

output = str(min_operation(data))

sys.stdout.write(output + '\n')