from itertools import permutations, starmap

# open(0) : 표준 입력 받아오기
NM, nums = [*open(0)]  # NM = "3 1\n", nums = "4 4 2\n"

# nums의 개행문자를 지우고 int로 변환해서 set에 넣은 후 정렬
sorted_set = sorted({*permutations(map(int, nums.split()), int(NM[2]))})  # {(2, 4, 4), (4, 2, 4), (4, 4, 2)}

for perm in sorted_set:
    print(*perm)
    
# 아래처럼 starmap 사용 가능
# *starmap(print,sorted({*permutations(map(int, nums.split()), int(NM[2]))})),