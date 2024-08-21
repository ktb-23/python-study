import sys
import heapq

def operation(x_s):
    min_heap = []
    results = []
    
    for x in x_s:  # x_s 안의 x들에 대해서
        if x == 0:  # x가 0이라면
            if min_heap:  # 힙이 비어있지 않다면
                results.append(heapq.heappop(min_heap))  # 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거
            else:  # 힙이 비어있으면
                results.append(0)  # 0 출력
        else:  # x가 0이 아닌 자연수라면
            heapq.heappush(min_heap, x)
    return results

# 입력 처리
input = sys.stdin.read
data = input().strip().splitlines()

# 첫째 줄: 연산의 개수 N
N = int(data[0])

# 다음 N줄: 연산에 대한 정보를 나타내는 정수 x
x_s = map(int, data[1:])

# 출력 결과
output = operation(x_s)
sys.stdout.write("\n".join(map(str, output)) + '\n')