import sys

# 절단기에 설정할 수 있는 높이의 최댓값을 찾는 함수
def find_max_height(lengths_trees, needed_meter):
    low, high = 0, max(lengths_trees)  # 탐색 범위의 시작과 끝점

    while low <= high:
        mid = (low + high) // 2
        # mid 높이로 잘랐을 때 얻을 수 있는 나무 길이의 합
        cut_sum = sum((length - mid) for length in lengths_trees if length > mid)
        
        if cut_sum >= needed_meter:
            # 필요한 나무보다 더 많이 잘라낼 수 있다면, 더 높은 높이로 시도
            low = mid + 1
        else:
            # 필요한 나무보다 덜 잘라내게 된다면, 높이를 낮춘다
            high = mid - 1
        
    return high  # 마지막으로 확인한 높이가 최대 가능 높이

# 입력 처리
input = sys.stdin.read
data = input().strip().splitlines()

# 첫째 줄: 나무의 수 N, 필요한 나무 길이 M
N, M = map(int, data[0].split())
# 둘째 줄: N개 나무들의 높이
trees = list(map(int, data[1].split()))

# 출력 결과
output = str(find_max_height(trees, M))
sys.stdout.write(output + '\n')