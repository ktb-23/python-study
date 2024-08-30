t = int(input())

for i in range(t):
    r, s = input().split()
    r = int(r)

    for alp in s:
        print(r * alp, end='')
    print()