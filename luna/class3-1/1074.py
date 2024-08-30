import sys

def z_order(N, r, c):
    # N이 0일 때 -> 0
    if N == 0:
        return 0
    
    # N이 0이 아닐 때
    half = 2 ** (N - 1)  # 사분면의 한 변의 길이
    
    # 사분면 결정
    if r < half and c < half:  # 좌측상단
        return z_order(N - 1, r, c)
    elif r < half and c >= half:  # 우측상단
        return half * half + z_order(N - 1, r, c - half)
    elif r >= half and c < half:  # 좌측하단
        return 2 * half * half + z_order(N - 1, r - half, c)
    else:  # 우측하단
        return 3 * half * half + z_order(N - 1, r - half, c - half)


# 입력 처리
input = sys.stdin.read
data = input().strip()

# 첫째 줄: 정수 N, r, c  (2**N, r행 c열)
N, r, c = map(int, data.split())

# 출력 결과
output = str(z_order(N, r, c))
sys.stdout.write(output + '\n')