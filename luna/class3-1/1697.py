import sys
from collections import deque

def shortest_time(n, k):
    # 수빈이가 동생보다 멀리 있다면 뒤로 걷기(n-1)밖에 하지 못함
    if n > k:
        return n - k

    # 나머지 경우에서는 n-1, n+1, n*2 총 3가지 가능
    # 방문 기록을 위한 리스트
    visited = [False] * 100_001 # 최대 길이가 100,000
    # 큐 초기화
    queue = deque([(n, 0)])
    visited[n] = True
    
    while queue:
        now_n, time = queue.popleft()
        
        # 동생을 찾은 경우
        if now_n == k:
            return time
        
        # 가능한 이동 경로
        next_move = [now_n - 1, now_n + 1, now_n * 2]
        
        for next_n in next_move:
            if 0 <= next_n <= 100_000 and not visited[next_n]:
                visited[next_n] = True
                queue.append((next_n, time + 1))
                
# 입력 처리
input = sys.stdin.read
data = input().strip()

# 첫째 줄: 정수 N, K  (수빈 위치 N, 동생 위치 K)
N, K = map(int, data.split())

# 출력 결과
output = str(shortest_time(N, K))
sys.stdout.write(output + '\n')