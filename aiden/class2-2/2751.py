import sys
input = sys.stdin.read

data = input().split()  
numbers = list(map(int, data[1:]))  

numbers.sort() 

print("\n".join(map(str, numbers)))
