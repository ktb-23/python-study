import sys

def new_coords(coords):  # 2 4 -10 4 -9
    # 중복 제거 및 좌표 정렬  {-10: 0, -9: 1, 2: 2, 4: 3}
    std_coords = {coord: idx for idx, coord in enumerate(sorted(set(coords)))}
    # 좌표 압축 리스트 생성 및 반환  [2, 3, 0, 3, 1]
    return [std_coords[coord] for coord in coords]

# 입력 처리
input = sys.stdin.read
data = input().strip().splitlines()

# 첫째 줄: 좌표의 개수 N
N = int(data[0])

# 둘째 줄: 공백 한 칸으로 구분된 좌표들  x1, x2, ... xn
x_s = list(map(int, data[1].split()))

# 출력 결과
output = " ".join(map(str, new_coords(x_s)))
sys.stdout.write(output + '\n')