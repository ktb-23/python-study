import sys


input = sys.stdin.readline

n = int(input().strip())  
n_list = list(map(int, input().strip().split()))  

m = int(input().strip()) 
m_list = list(map(int, input().strip().split()))

n_set = set(n_list)
answer = []

for element in m_list:
    if element in n_set:
        answer.append('1')
    else:
        answer.append('0')

print('\n'.join(answer))
