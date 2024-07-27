while True:
    n = int(input())
    reversed_n = int(str(n)[::-1])
    if n == 0:
        break
    elif n == reversed_n:
        print("yes")
    else:
        print("no")