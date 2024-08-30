def move(n,r,c):
    if n == 0:
        return 0
    half = 2**(n-1)
    # 각 사분면
    if r < half and c < half:
        return move(n-1, r, c)
    elif r < half and c >= half:
        return half * half + move(n-1, r, c-half)
    elif r >= half and c < half:
        return 2 * half * half + move(n-1, r-half, c)
    else:
        return 3 * half * half + move(n-1, r-half, c-half)

n, r, c = map(int,input().split())
print(move(n,r,c))