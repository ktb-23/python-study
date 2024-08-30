import sys


def count_paper(x, y, size):
    # 첫 번째 칸의 색을 기준으로 모두 같은 색인지 확인
    first_color = paper[x][y]
    all_same_color = True
    
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != first_color:
                all_same_color = False
                break
        if not all_same_color:
            break
    
    # 색이 모두 같다면 해당 색의 카운트를 증가
    if all_same_color:
        color_count[first_color] += 1
        return
    
    # 색이 같지 않다면 네 부분으로 나누어 재귀적으로 탐색
    half_size = size // 2
    count_paper(x, y, half_size)
    count_paper(x, y + half_size, half_size)
    count_paper(x + half_size, y, half_size)
    count_paper(x + half_size, y + half_size, half_size)


# 입력 처리
input = sys.stdin.read
data = input().strip().splitlines()

# 첫째 줄: 전체 종이 한 변의 길이
N = int(data[0])  # 최대 크기: 128 * 128
# 다음 N줄: 색종이의 각 가로줄의 색
paper = [list(map(int, line.split())) for line in data[1:]]
color_count = [0, 0]

# 함수 시작. 시작 지점 (0, 0), 길이 N
count_paper(0, 0, N)

# 출력 결과
output = "\n".join(str(cnt) for cnt in color_count)
sys.stdout.write(output + '\n')