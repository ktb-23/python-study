import sys

input = sys.stdin.read

def solve():
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    
    unheard = set(data[2:2+n])
    
    both_unseen = set()
    for name in data[2+n:]:
        if name in unheard:
            both_unseen.add(name)
    
    both_unseen = sorted(both_unseen)
    print(len(both_unseen))
    for name in both_unseen:
        print(name)
solve()