from itertools import permutations

n, m = map(int,input().split()) 
n_list = list(map(int,input().split()))    
perm = permutations(sorted(n_list), m)

unique_perm = sorted(set(perm))

for p in unique_perm:
    print(' '.join(map(str, p)))