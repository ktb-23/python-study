# 문제
# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고,
# 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 
# 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
# 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.
# 
# 수빈이와 동생의 위치가 주어졌을 때, 
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
# 
# 입력
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
# 
# 출력
# 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
from collections import deque

def walk(x):
    return [x-1,x+1]

def tel(x):
    return x * 2

def bfs(n,k):
    max_limit = 100001
    visit = [False] * max_limit
    distance = [0] * max_limit

    queue = deque([n])
    visit[n] = True

    while queue:
        current = queue.popleft()

        if current == k:
            return distance[current]

        # 순간이동 처리 (0초 걸림)
        next_pos = tel(current)
        if 0 <= next_pos < max_limit and not visit[next_pos]:
            visit[next_pos] = True
            distance[next_pos] = distance[current]
            queue.appendleft(next_pos)  # 순간이동은 우선순위를 높이기 위해 앞에 추가

        # 걷기 처리 (1초 걸림)
        for next_pos in walk(current):
            if 0 <= next_pos < max_limit and not visit[next_pos]:
                visit[next_pos] = True
                distance[next_pos] = distance[current] + 1
                queue.append(next_pos)

n, k = map(int, input().split())
print(bfs(n, k))
