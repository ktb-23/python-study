import sys

def max_meeting(meeting_times):  # [(1, 4), (1, 2), (2, 5), (3, 5)]
    # 회의 끝나는 시간을 기준으로 정렬. 끝나는 시간이 같으면 시작 시간이 빠른 순서대로 정렬
    meeting_times.sort(key=lambda x: (x[1], x[0]))  # [(1, 2), (1, 4), (2, 5), (3, 5)]
    
    count = 0  # 회의 개수
    end_time = 0  # 마지막으로 종료된 회의의 종료 시각
    
    for start, end in meeting_times:  # 각 튜플의 시작, 종료 시간에 대해
        if start >= end_time:  # 회의 시작 시간이 마지막 회의 종료 시간 이후라면
            count += 1  # 회의 개수 카운트 +1
            end_time = end  # 현재 회의의 종료 시간을 마지막 종료 시간으로 갱신

    return count  # for 구문이 끝났을 때 최대 회의 개수 반환

# 입력 처리
input = sys.stdin.read
data = input().strip().splitlines()

# 첫째 줄: 회의의 수
N = int(data[0])

# 다음 N줄: 각 회의의 정보 ('회의 시작 시간' '회의 끝 시간')
times = [tuple(map(int, line.strip().split())) for line in data[1:N+1]]

# 출력 결과
output = str(max_meeting(times))
sys.stdout.write(output + '\n')