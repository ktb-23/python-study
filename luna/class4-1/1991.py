N, *lines = open(0).read().splitlines()  # 줄마다 읽어옴, n = 7, lines = ['A B C', ...]
data = {a: (b, c) for a, b, c in (line.split() for line in lines)}  # {'A': ('B', 'C'), ...}

def order_n1(i):  # 전위 순회
    print(i, end='')  # 루트 출력
    left, right = data[i]
    if left != '.':
        order_n1(left)  # 왼쪽 자식 순회
    if right != '.':
        order_n1(right)  # 오른쪽 자식 순회

def order_n2(i):  # 중위 순회
    left, right = data[i]
    if left != '.':
        order_n2(left)  # 왼쪽 자식 순회
    print(i, end='')  # 루트 출력
    if right != '.':
        order_n2(right)  # 오른쪽 자식 순회

def order_n3(i):  # 후위 순회
    left, right = data[i]
    if left != '.':
        order_n3(left)  # 왼쪽 자식 순회
    if right != '.':
        order_n3(right)  # 오른쪽 자식 순회
    print(i, end='')  # 루트 출력
        
order_n1('A')
print()
order_n2('A')
print()
order_n3('A')